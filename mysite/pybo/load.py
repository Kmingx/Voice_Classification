
from tensorflow import keras
from django.apps import AppConfig


class LoadConfig(AppConfig):
    rod_model = keras.models.load_model("C:/src/DjangoStudy/model/model.h5")

    def ready(self):
        pass