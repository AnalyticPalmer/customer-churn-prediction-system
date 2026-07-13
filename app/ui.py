"""
User Interface Module
=====================

Creates the sidebar and collects customer information
for the Customer Churn Prediction System.

Author: Palmer Ogiriki
Version: 2.0
"""

# ==========================================================
# Imports
# ==========================================================

import pandas as pd
import streamlit as st


# ==========================================================
# Collect User Input
# ==========================================================

def get_user_input():
    """
    Collect customer information from the sidebar.

    Returns
    -------
    pandas.DataFrame
        Customer information formatted for prediction.
    """

    # ======================================================
    # Sidebar Title
    # ======================================================

    st.sidebar.title("📝 Customer Information")

    st.sidebar.markdown(
        "Fill in the customer details below, then click **Predict Churn**."
    )

    st.sidebar.divider()

    # ======================================================
    # Personal Information
    # ======================================================

    st.sidebar.subheader("👤 Personal Details")

    gender = st.sidebar.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    senior = st.sidebar.selectbox(
        "Senior Citizen",
        [0, 1],
        help="0 = No, 1 = Yes"
    )

    partner = st.sidebar.selectbox(
        "Partner",
        ["Yes", "No"]
    )

    dependents = st.sidebar.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

    tenure = st.sidebar.slider(
        "Tenure (Months)",
        min_value=0,
        max_value=72,
        value=24
    )

    st.sidebar.divider()

    # ======================================================
    # Services
    # ======================================================

    st.sidebar.subheader("📡 Services")

    phone_service = st.sidebar.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    multiple_lines = st.sidebar.selectbox(
        "Multiple Lines",
        [
            "Yes",
            "No",
            "No phone service"
        ]
    )

    internet_service = st.sidebar.selectbox(
        "Internet Service",
        [
            "DSL",
            "Fiber optic",
            "No"
        ]
    )

    online_security = st.sidebar.selectbox(
        "Online Security",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    online_backup = st.sidebar.selectbox(
        "Online Backup",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    device_protection = st.sidebar.selectbox(
        "Device Protection",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    tech_support = st.sidebar.selectbox(
        "Tech Support",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    streaming_tv = st.sidebar.selectbox(
        "Streaming TV",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    streaming_movies = st.sidebar.selectbox(
        "Streaming Movies",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    st.sidebar.divider()

    # ======================================================
    # Billing
    # ======================================================

    st.sidebar.subheader("💳 Billing Information")

    contract = st.sidebar.selectbox(
        "Contract",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )

    paperless = st.sidebar.selectbox(
        "Paperless Billing",
        [
            "Yes",
            "No"
        ]
    )

    payment = st.sidebar.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

    monthly = st.sidebar.number_input(
        "Monthly Charges",
        min_value=0.0,
        max_value=200.0,
        value=70.00,
        step=0.01
    )

    total = st.sidebar.number_input(
        "Total Charges",
        min_value=0.0,
        value=1500.00,
        step=0.01
    )

    st.sidebar.divider()

    st.sidebar.info(
        """
**Model Information**

- Model: XGBoost
- Version: 2.0
- Dataset: Telco Customer Churn
"""
    )

    # ======================================================
    # Return DataFrame
    # ======================================================

    customer = pd.DataFrame({
        "gender": [gender],
        "SeniorCitizen": [senior],
        "Partner": [partner],
        "Dependents": [dependents],
        "tenure": [tenure],
        "PhoneService": [phone_service],
        "MultipleLines": [multiple_lines],
        "InternetService": [internet_service],
        "OnlineSecurity": [online_security],
        "OnlineBackup": [online_backup],
        "DeviceProtection": [device_protection],
        "TechSupport": [tech_support],
        "StreamingTV": [streaming_tv],
        "StreamingMovies": [streaming_movies],
        "Contract": [contract],
        "PaperlessBilling": [paperless],
        "PaymentMethod": [payment],
        "MonthlyCharges": [monthly],
        "TotalCharges": [total]
    })

    return customer