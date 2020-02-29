import pandas as pd
from feature_extractor import feature_extractor

def extract_features(dataframe):
    ft = feature_extractor(dataframe)
    features = ft.extract_features()
    return features

def pre_process_dataframe(dataframe):
    #dropping unwanted columns
    dataframe = dataframe.drop(["Url","domain","query","path","file_ext", "decoded_query_values"], axis = 1)
    #changing string values to numeric
    dataframe = dataframe.apply(pd.to_numeric, errors='coerce')
    #filling null values
    dataframe.fillna(0, inplace=True)
    return dataframe

def url_to_features(url):
    data = {'Url': [url]}

    dataframe = pd.read_json(data)

    dataframe = extract_features(dataframe)
    dataframe = pre_process_dataframe(dataframe)

    dataframe.to_json()