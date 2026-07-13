"""
Prediction Module
=================

Handles all prediction logic for the Customer Churn Prediction System.

Author: Palmer Ogiriki
Version: 2.0
"""

# ==========================================================
# Imports
# ==========================================================

import pandas as pd


# ==========================================================
# Prediction Function
# ==========================================================

def predict_churn(model, preprocessor, customer_data):
    """
    Predict whether a customer is likely to churn.

    Parameters
    ----------
    model : object
        Trained machine learning model.

    preprocessor : object
        Saved preprocessing pipeline.

    customer_data : pandas.DataFrame
        Customer information entered through the Streamlit app.

    Returns
    -------
    tuple
        prediction : str
            "Yes" or "No"

        probability : float
            Probability that the customer will churn.

        confidence : float
            Confidence of the prediction.
    """

    # ------------------------------------------------------
    # Validate Input
    # ------------------------------------------------------

    if not isinstance(customer_data, pd.DataFrame):
        raise TypeError(
            "customer_data must be a pandas DataFrame."
        )

    # ------------------------------------------------------
    # Transform Data
    # ------------------------------------------------------

    processed_data = preprocessor.transform(customer_data)

    # ------------------------------------------------------
    # Model Prediction
    # ------------------------------------------------------

    prediction = model.predict(processed_data)[0]

    probability = model.predict_proba(processed_data)[0][1]

    # ------------------------------------------------------
    # Convert Prediction
    # ------------------------------------------------------

    if prediction in [1, "Yes"]:
        prediction_label = "Yes"
    else:
        prediction_label = "No"

    # ------------------------------------------------------
    # Confidence Score
    # ------------------------------------------------------

    confidence = max(probability, 1 - probability)

    # ------------------------------------------------------
    # Return Results
    # ------------------------------------------------------

    return (
        prediction_label,
        probability,
        confidence
    )


# ==========================================================
# Prediction Summary
# ==========================================================

def create_prediction_summary(prediction, probability):
    """
    Create a readable prediction summary.

    Parameters
    ----------
    prediction : str

    probability : float

    Returns
    -------
    str
    """

    probability_percent = probability * 100

    if prediction == "Yes":

        return (
            f"The customer is likely to churn "
            f"with a probability of "
            f"{probability_percent:.2f}%."
        )

    return (
        f"The customer is unlikely to churn. "
        f"The estimated churn probability is "
        f"{probability_percent:.2f}%."
    )