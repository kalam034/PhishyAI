import pandas as pd

from sklearn.externals.joblib import load
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score


def test_random_forest(X_test, y_test):
    rf = load("models/random_forest.joblib")
    extract_metrics(rf, X_test, y_test, "Random Forest")


def test_gradient_boosting_trees_model(X_test, y_test):
    gbt = load("models/gradient_boosting_trees.joblib")
    extract_metrics(gbt, X_test, y_test, "Gradient Boosting Tree")


def test_logistic_regression(X_test, y_test):
    lgt = load("models/logistic_regression.joblib")
    extract_metrics(lgt, X_test, y_test, "Logistic Regression")


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


def test_models():
    print('\n')
    print("Testing the models")

    X_test = pd.read_csv("data/interim/X_test.csv",
                         header=0, low_memory=False).to_numpy()
    y_test = pd.read_csv("data/interim/y_test.csv",
                         header=0, low_memory=False).to_numpy()

    test_random_forest(X_test, y_test)
    test_gradient_boosting_trees_model(X_test, y_test)
    test_logistic_regression(X_test, y_test)
