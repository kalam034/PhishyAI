import os

from .data import make_dataset as mk
from .features import build_features as ft
from .models import train_models as train
from .models import test_models as test


def run_pipeline():
    os.chdir(os.path.dirname(__file__))

    mk.make_dataset()
    ft.generate_features()
    train.train_models()
    test.test_models()
