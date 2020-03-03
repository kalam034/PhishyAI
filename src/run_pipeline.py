import data.make_dataset as mk
import features.bulid_features as ft
import models.train_models as train
import models.test_models as test

mk.make_dataset()
ft.extract_features()
train.train_models()
test.test_models()
