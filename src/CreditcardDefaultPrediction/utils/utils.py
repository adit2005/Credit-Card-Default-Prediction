import os
import sys
import pickle

from src.CreditcardDefaultPrediction.logger import logging
from src.CreditcardDefaultPrediction.exception import CustomException

from sklearn.metrics import accuracy_score

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        logging.info("Exception occurred in save_object method")
        raise CustomException(e, sys)


def evaluate_model(y_true, y_pred):
    try:
        return accuracy_score(y_true, y_pred)

    except Exception as e:
        logging.info("Exception occurred in evaluate_model function")
        raise CustomException(e, sys)


def load_object(file_path):
    try:

        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        logging.info("Exception occurred in loading object")
        raise CustomException(e, sys)