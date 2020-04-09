import os
from sklearn.externals import joblib


class ProbabilityPredictor(object):
    def __init__(self, model):
        self._model = model

    def predict(self, instances, **kwargs):
        probabilities = self._model.predict_proba(instances)
        return probabilities.tolist()

    @classmethod
    def from_path(cls, model_dir):
        model_path = os.path.join(model_dir, 'model.joblib')
        model = joblib.load(model_path)

        return cls(model)
