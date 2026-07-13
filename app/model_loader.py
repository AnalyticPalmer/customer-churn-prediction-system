"""
Model Loader
============

Loads the trained machine learning model
and preprocessing pipeline.

Author: Palmer Ogiriki
Version: 2.0
"""

import joblib

from config import (
    MODEL_FILE,
    PREPROCESSOR_FILE
)


def load_model():
    """
    Load the trained model and preprocessor.

    Returns
    -------
    tuple
        model,
        preprocessor
    """

    model = joblib.load(MODEL_FILE)

    preprocessor = joblib.load(PREPROCESSOR_FILE)

    return model, preprocessor