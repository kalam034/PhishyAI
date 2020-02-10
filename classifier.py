import pandas as pd

from feature_extractor import feature_extractor


def print_number_records(dataframe):
    
    bn_records = dataframe.loc[dataframe ['Label'] == 0]
    ml_records = dataframe.loc[dataframe ['Label'] == 1]

    print("Total number of records in training dataframe: " + str(dataframe.shape[0]))
    print("Total number of benign records in training dataframe: + " + str(bn_records.shape[0]))
    print("Total number of malicious records in training dataframe: + " + str(ml_records.shape[0]))


if __name__ == "__main__":

    df = pd.read_csv("training_datasets/merged_dataframes_100.csv", header = 0)

    ft = feature_extractor(df)
    df_features = ft.extract_features()
    df_features.to_csv("training_datasets/dataframe_with_features.csv")
    





    
