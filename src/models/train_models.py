import pandas as pd

from sklearn.externals.joblib import dump
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.utils.testing import ignore_warnings


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


def train_rfc(X_train, y_train):
    rfc = RandomForestClassifier(n_estimators=5, random_state=42)
    return rfc.fit(X_train, y_train)


def train_gbt(X_train, y_train):
    gbt = GradientBoostingClassifier(max_depth=3)
    return gbt.fit(X_train, y_train)


@ignore_warnings()  # line convergence warnings ignored
def train_lgt(X_train, y_train):
    lgt = LogisticRegression(max_iter=100, solver='newton-cg')
    return lgt.fit(X_train, y_train)


if __name__ == "__main__":
    dataframe = pd.read_csv(
        "../../data/processed/features.csv", header=0, low_memory=False)

    print_number_of_records(dataframe)

    X = dataframe.drop("Label", axis=1)
    y = dataframe["Label"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    X_train = X_train.to_numpy()
    y_train = y_train.to_numpy()

    X_test = X_test.to_csv(
        "../../data/interim/X_test.csv", index=False, header=True)
    y_test = y_test.to_csv(
        "../../data/interim/y_test.csv", index=False, header=True)

    # training

    # random forest
    rf = train_rfc(X_train, y_train)
    dump(rf, "../../models/random_forest.joblib")

    # logistic regression
    lgt = train_lgt(X_train, y_train)
    dump(lgt, "../../models/logistic_regression.joblib")

    # gradient boosting
    gbt = train_gbt(X_train, y_train)
    dump(gbt, "../../models/gradient_boosting_trees.joblib")
