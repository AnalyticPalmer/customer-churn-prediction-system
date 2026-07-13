"""
Utility Functions
=================

Reusable helper functions for the Customer Churn Prediction System.

Author: Palmer Ogiriki
Version: 2.0
"""

# ==========================================================
# Imports
# ==========================================================

from datetime import datetime
import pandas as pd


# ==========================================================
# Probability Formatter
# ==========================================================

def format_probability(probability):
    """
    Convert probability into percentage format.

    Example:
        0.82345 -> 82.35%
    """

    return f"{probability:.2%}"


# ==========================================================
# Confidence Formatter
# ==========================================================

def format_confidence(confidence):
    """
    Format confidence score.

    Example:
        0.9544 -> 95.44%
    """

    return f"{confidence:.2%}"


# ==========================================================
# Risk Level
# ==========================================================

def get_risk_level(probability):
    """
    Determine churn risk level.
    """

    if probability < 0.30:
        return "🟢 Low"

    elif probability < 0.70:
        return "🟡 Medium"

    else:
        return "🔴 High"


# ==========================================================
# Prediction Status
# ==========================================================

def get_prediction_status(prediction):
    """
    Return a readable prediction message.
    """

    if prediction == "Yes":
        return "Customer is likely to churn."

    return "Customer is unlikely to churn."


# ==========================================================
# Prediction Color
# ==========================================================

def get_prediction_color(prediction):
    """
    Return UI color for prediction.
    """

    if prediction == "Yes":
        return "red"

    return "green"


# ==========================================================
# Display Customer Data
# ==========================================================

def display_customer_data(customer):
    """
    Format customer information for display.

    Converts all values to strings to avoid PyArrow
    type conversion errors in Streamlit.
    """

    display_df = customer.T.rename(
        columns={0: "Value"}
    )

    display_df["Value"] = display_df["Value"].astype(str)

    return display_df


# ==========================================================
# Current Timestamp
# ==========================================================

def get_timestamp():
    """
    Return current date and time.
    """

    return datetime.now().strftime(
        "%d %B %Y %I:%M %p"
    )


# ==========================================================
# Create Prediction Report
# ==========================================================

def create_prediction_report(
    customer,
    prediction,
    probability,
    confidence
):
    """
    Create downloadable prediction report.
    """

    report = customer.copy()

    report["Prediction"] = prediction

    report["Risk Level"] = get_risk_level(
        probability
    )

    report["Probability"] = format_probability(
        probability
    )

    report["Confidence"] = format_confidence(
        confidence
    )

    report["Prediction Time"] = get_timestamp()

    return report.to_csv(
        index=False
    ).encode("utf-8")


# ==========================================================
# Prediction Insights
# ==========================================================

def get_prediction_insights(customer):
    """
    Generate rule-based prediction insights.
    """

    insights = []

    if customer["Contract"].iloc[0] == "Month-to-month":
        insights.append(
            "• Month-to-month contracts are associated with higher churn."
        )

    if customer["InternetService"].iloc[0] == "Fiber optic":
        insights.append(
            "• Fiber optic customers historically show higher churn."
        )

    if customer["PaymentMethod"].iloc[0] == "Electronic check":
        insights.append(
            "• Electronic check payments have been linked with higher churn."
        )

    if customer["tenure"].iloc[0] < 12:
        insights.append(
            "• Customers with short tenure are more likely to churn."
        )

    if customer["OnlineSecurity"].iloc[0] == "No":
        insights.append(
            "• Customers without Online Security tend to churn more often."
        )

    if customer["TechSupport"].iloc[0] == "No":
        insights.append(
            "• Lack of Tech Support is associated with increased churn."
        )

    if not insights:
        insights.append(
            "• No major churn risk indicators were detected."
        )

    return insights


# ==========================================================
# Dashboard Metrics
# ==========================================================

def dashboard_metrics():
    """
    Return dashboard information.
    """

    return {
        "Model": "XGBoost",
        "Version": "2.0",
        "Dataset": "Telco Customer Churn",
        "Framework": "Streamlit"
    }