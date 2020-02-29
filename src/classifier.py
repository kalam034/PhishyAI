import pandas as pd

from sklearn.externals.joblib import dump, load
from features.feature_extractor import feature_extractor

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, IsolationForest
from sklearn.svm import OneClassSVM
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.utils.testing import ignore_warnings


def print_number_of_records(dataframe):
    bn_records = dataframe.loc[dataframe['Label'] == 0]
    ml_records = dataframe.loc[dataframe['Label'] == 1]

    print('\n')
    print("Total number of records in the dataframe: ", str(dataframe.shape[0]))
    print("Total number of benign records in the dataframe: ", str(bn_records.shape[0]))
    print("Total number of malicious records in the dataframe: ", str(ml_records.shape[0]))


def extract_features(dataframe):
    ft = feature_extractor(dataframe)
    features = ft.extract_features()
    return features


def pre_process_dataframe(dataframe):
    # dropping unwanted columns
    dataframe = dataframe.drop(["Url", "domain", "query", "path", "file_ext", "decoded_query_values"], axis=1)
    # changing string values to numeric
    dataframe = dataframe.apply(pd.to_numeric, errors='coerce')
    # filling null values
    dataframe.fillna(0, inplace=True)
    return dataframe


def train_rfc(X_train, y_train):
    rfc = RandomForestClassifier(n_estimators=5, random_state=42)
    return rfc.fit(X_train, y_train)


def train_gbt(X_train, y_train):
    gbt = GradientBoostingClassifier(max_depth=3)
    return gbt.fit(X_train, y_train)


@ignore_warnings()  # line convergence warnings ignored
def train_lgt(X_train, y_train):
    lgt = LogisticRegression(max_iter=200, solver='newton-cg')
    return lgt.fit(X_train, y_train)


def extract_metrics(model, X_test, y_test, model_name):
    pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, pred)
    f1 = f1_score(y_test, pred)
    recall = recall_score(y_test, pred)
    precision = precision_score(y_test, pred)

    print('\n')
    print(model_name + " accuracy score: %.3f" % accuracy)
    print(model_name + " f1 score: %.3f" % f1)
    print(model_name + " recall score: %.3f" % recall)
    print(model_name + " precision score: %.3f" % precision)


def save_model(model, path):
    dump(model, path)


def load_model(path):
    return load(path)


if __name__ == "__main__":
    dataframe = pd.read_csv("../data/interim/final_merged_dataframes.csv", header=0)

    print_number_of_records(dataframe)

    dataframe = extract_features(dataframe)

    dataframe = pre_process_dataframe(dataframe)
    # splitting the data for training and testing
    X = dataframe.drop("Label", axis=1)
    y = dataframe["Label"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    X_train = X_train.to_numpy()
    X_test = X_test.to_numpy()
    y_train = y_train.to_numpy()
    y_test = y_test.to_numpy()

    # training and testing classifiers

    # random forest
    rf = train_rfc(X_train, y_train)
    extract_metrics(rf, X_test, y_test, "Random Forest")

    # gradient boosting
    gbt = train_gbt(X_train, y_train)
    extract_metrics(gbt, X_test, y_test, "Gradient Boosting ")

    # logistic regression
    lgt = train_lgt(X_train, y_train)

    extract_metrics(lgt, X_test, y_test, "Logistic Regression")
    save_model(lgt, "../models/model.joblib")
