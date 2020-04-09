import pandas as pd


def read_open_phish():
    open_phish_df = pd.read_csv("data/raw/open_phish.txt", names=["Url"])
    open_phish_df['Label'] = 0

    return open_phish_df


def read_phish_storm():
    phish_storm_df = pd.read_csv("data/raw/phish_storm.csv", skipinitialspace=True, encoding="ISO-8859-1",
                                 low_memory=False, usecols=["domain", "label"])
    phish_storm_df.columns = ["Url", "Label"]
    phish_storm_df = phish_storm_df.drop(
        phish_storm_df[(phish_storm_df.Label != "1.0") & (phish_storm_df.Label != "0.0")].index)
    phish_storm_df["Url"] = phish_storm_df["Url"].map(
        lambda x: x.replace("'", ''))
    phish_storm_df.Label = phish_storm_df.Label.astype(float)

    return phish_storm_df


def read_unb():
    unb_phish_df = pd.read_csv("data/raw/unb_phish.txt", names=["Url"])
    unb_benign_df = pd.read_csv("data/raw/unb_benign.txt", names=["Url"])

    unb_phish_df["Label"] = 0
    unb_benign_df["Label"] = 1

    return pd.concat([unb_phish_df, unb_benign_df], sort=True, axis=0)


def read_phish_tank():
    phish_tank_df = pd.read_csv("data/raw/phish_tank.csv",
                                skipinitialspace=True, usecols=["phish_detail_url"])
    phish_tank_df.columns = ["Url"]
    phish_tank_df["Label"] = 0

    return phish_tank_df


def read_benign():
    benign_data_df = pd.read_csv(
        "data/raw/data-benign.csv", skipinitialspace=True, usecols=["link"])
    benign_data_df.columns = ["Url"]
    benign_data_df["Label"] = 0

    more_benign_data_df = pd.read_csv(
        "data/raw/data_more_benign.csv", skipinitialspace=True, usecols=["url"])
    more_benign_data_df.columns = ["Url"]
    more_benign_data_df["Label"] = 0

    return pd.concat([benign_data_df, more_benign_data_df], sort=True, axis=0)


def read_malicious():
    malicious_data_df = pd.read_csv(
        "data/raw/data-malicious.csv", skipinitialspace=True, usecols=["link"])
    malicious_data_df.columns = ["Url"]
    malicious_data_df["Label"] = 1

    return malicious_data_df


def make_dataset():
    print('\n')
    print("Collecting data from all data sources")

    open_phish_df = read_open_phish()
    phish_storm_df = read_phish_storm()
    unb_df = read_unb()
    phish_tank_df = read_phish_tank()
    benign_df = read_benign()
    malicious_df = read_malicious()

    print("Merging all collected data")

    merged_df = pd.concat([open_phish_df, unb_df, phish_storm_df, phish_tank_df,
                           benign_df, malicious_df], sort=True, axis=0)

    merged_df = merged_df.sample(frac=1).reset_index(drop=True)
    merged_df = merged_df.drop_duplicates(inplace=False)

    
    merged_df.to_csv("data/interim/final_merged_dataframes.csv",
                     encoding='utf-8', header=True, index=False)
