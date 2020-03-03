import pandas as pd

from . import bulid_features as ft


def url_to_features(url):
    data = {'Url': [url]}

    dataframe = pd.read_json(data)

    dataframe = ft.extract_features_df(dataframe)

    dataframe.to_numpy()
