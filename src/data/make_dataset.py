import pandas as pd


def print_number_of_records(dataframe):
    bn_records = dataframe.loc[dataframe['Label'] == 0]
    ml_records = dataframe.loc[dataframe['Label'] == 1]

    print('\n')
    print("Total number of records in the dataframe: ",
          str(dataframe.shape[0]))
    print("Total number of benign records in the dataframe: ",
          str(bn_records.shape[0]))
    print("Total number of malicious records in the dataframe: ",
          str(ml_records.shape[0]))


def read_open_phish():
    open_phish_DF = pd.read_csv("../../data/raw/open_phish.txt", names=["Url"])
    open_phish_DF['Label'] = 0

    return open_phish_DF


def read_phish_storm():
    phish_storm_DF = pd.read_csv("../../data/raw/phish_storm.csv", skipinitialspace=True, encoding="ISO-8859-1",
                                 low_memory=False, usecols=["domain", "label"])
    phish_storm_DF.columns = ["Url", "Label"]
    phish_storm_DF = phish_storm_DF.drop(
        phish_storm_DF[(phish_storm_DF.Label != "1.0") & (phish_storm_DF.Label != "0.0")].index)
    phish_storm_DF["Url"] = phish_storm_DF["Url"].map(
        lambda x: x.replace("'", ''))
    phish_storm_DF.Label = phish_storm_DF.Label.astype(float)

    return phish_storm_DF


def read_unb():
    unb_phish_DF = pd.read_csv("../../data/raw/unb_phish.txt", names=["Url"])
    unb_benign_DF = pd.read_csv("../../data/raw/unb_benign.txt", names=["Url"])

    unb_phish_DF["Label"] = 0
    unb_benign_DF["Label"] = 1

    return pd.concat([unb_phish_DF, unb_benign_DF], sort=True, axis=0)


def read_phish_tank():
    phish_tank_DF = pd.read_csv("../../data/raw/phish_tank.csv",
                                skipinitialspace=True, usecols=["phish_detail_url"])
    phish_tank_DF.columns = ["Url"]
    phish_tank_DF["Label"] = 0

    return phish_tank_DF


def read_benign():
    benign_data_DF = pd.read_csv(
        "../../data/raw/data-benign.csv", skipinitialspace=True, usecols=["link"])
    benign_data_DF.columns = ["Url"]
    benign_data_DF["Label"] = 0

    more_benign_data_DF = pd.read_csv(
        "../../data/raw/data_more_benign.csv", skipinitialspace=True, usecols=["url"])
    more_benign_data_DF.columns = ["Url"]
    more_benign_data_DF["Label"] = 0

    return pd.concat([benign_data_DF, more_benign_data_DF], sort=True, axis=0)


def read_malcious():
    malcious_data_DF = pd.read_csv(
        "../../data/raw/data-malicious.csv", skipinitialspace=True, usecols=["link"])
    malcious_data_DF.columns = ["Url"]
    malcious_data_DF["Label"] = 1

    return malcious_data_DF


def merge_dataframes():
    open_phish_DF = read_open_phish()
    phish_storm_DF = read_phish_storm()
    unb_DF = read_unb()
    phish_tank_DF = read_phish_tank()
    benign_DF = read_benign()
    malcious_DF = read_malcious()

    merged_DF = pd.concat([open_phish_DF, unb_DF, phish_storm_DF, phish_tank_DF,
                           benign_DF, malcious_DF], sort=True, axis=0)

    merged_DF = merged_DF.sample(frac=1).reset_index(drop=True)
    merged_DF = merged_DF.drop_duplicates(inplace=False)

    merged_DF.to_csv("../../data/interim/final_merged_dataframes.csv",
                     encoding='utf-8', header=True, index=False)

    return merged_DF


if __name__ == "__main__":
    dataframe = merge_dataframes()
    print_number_of_records(dataframe)
    dataframe.to_csv("../../data/interim/final_merged_dataframes.csv",
                     encoding='utf-8', header=True, index=False)
