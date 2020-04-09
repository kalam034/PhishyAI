from src.data import make_dataset as mk
from src.features import build_features as ft
from src.models import train_models as train
from src.models import test_models as test

if __name__ == '__main__':
    
    mk.make_dataset()
    ft.generate_features()
    train.train_models()
    test.test_models()