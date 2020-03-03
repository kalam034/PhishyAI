import bulid_features as ft
import pandas as pd


def url_to_features(url):
    data = {'Url': [url]}

    dataframe = pd.read_json(data)

    dataframe = ft.extract_features(dataframe)

    dataframe.to_numpy()
