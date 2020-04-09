from flask import jsonify
import pandas as pd
import features.build_features as ft


def get_features_from_urls(request):
    try:
        print("Starting get_features_from_urls")
        request_json = request.get_json()
        urls = request_json["urls"]
        print("Got request to classify [%d] URLs" % len(urls))

        dataframe = pd.DataFrame({"Url": urls})
        features = ft.extract_features(dataframe).to_numpy()

        print("Features extracted, formatting and responding")
        response = [row.tolist() for row in features]
        return jsonify(response)
    except Exception as exception:
        print("Unable to get features")
        print(exception)
        return "", 500
