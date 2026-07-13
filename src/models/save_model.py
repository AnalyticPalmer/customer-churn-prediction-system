"""
Utilities for saving trained models.
"""

import joblib
import os


def save_model(model, filename):
    """
    Save a trained model.
    """

    model_path = os.path.join(
        "..",
        "models",
        filename
    )

    joblib.dump(model, model_path)

    print(f"Model saved to {model_path}")