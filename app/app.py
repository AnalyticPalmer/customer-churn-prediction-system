"""

Customer Churn Prediction System

================================



Main Streamlit Application



Author: Palmer Ogiriki

Version: 2.0

"""



# ==========================================================

# Imports

# ==========================================================



import streamlit as st



from model_loader import load_model

from prediction import (

    predict_churn,

    create_prediction_summary

)



from ui import get_user_input



from styles import load_css



from utils import (

    format_probability,

    format_confidence,

    get_risk_level,

    get_prediction_status,

    display_customer_data,

    create_prediction_report,

    get_prediction_insights,

    dashboard_metrics,

    get_timestamp

)



# ==========================================================

# Page Configuration

# ==========================================================



st.set_page_config(

    page_title="Customer Churn Prediction System",

    page_icon="📊",

    layout="wide",

    initial_sidebar_state="expanded"

)



# ==========================================================

# Load Custom CSS

# ==========================================================



load_css()



# ==========================================================

# Load Machine Learning Model

# ==========================================================



try:



    model, preprocessor = load_model()



except Exception as e:



    st.error(

        "Unable to load the trained machine learning model."

    )



    st.exception(e)



    st.stop()



# ==========================================================

# Dashboard Header

# ==========================================================



st.title("📊 Customer Churn Prediction System")



st.markdown(

    """

Welcome to **Customer Churn Prediction System Version 2.0**.



This application predicts whether a customer is likely to churn using a

trained **XGBoost Machine Learning Model**.



Complete the customer information from the sidebar and click

**Predict Churn** to generate a prediction.

"""

)



# ==========================================================

# Dashboard Metrics

# ==========================================================



metrics = dashboard_metrics()



metric1, metric2, metric3, metric4 = st.columns(4)



metric1.metric(

    "Model",

    metrics["Model"]

)



metric2.metric(

    "Version",

    metrics["Version"]

)



metric3.metric(

    "Dataset",

    metrics["Dataset"]

)



metric4.metric(

    "Framework",

    metrics["Framework"]

)



st.divider()



# ==========================================================

# Sidebar Input

# ==========================================================



customer = get_user_input()



# ==========================================================

# Prediction Section

# ==========================================================



predict_button = st.sidebar.button(

    "🚀 Predict Churn",

    use_container_width=True

)



# ==========================================================

# Wait For Prediction

# ==========================================================



if predict_button:



    with st.spinner(

        "Running prediction..."

    ):



        try:



            (

                prediction,

                probability,

                confidence

            ) = predict_churn(



                model,

                preprocessor,

                customer



            )



            report = create_prediction_report(



                customer,

                prediction,

                probability,

                confidence



            )



            summary = create_prediction_summary(



                prediction,

                probability



            )



            insights = get_prediction_insights(

                customer

            )



            timestamp = get_timestamp()



            st.divider()



            left_column, right_column = st.columns(

                [1.2, 1]

            )



            # ==========================================================

            # Left Column - Prediction Results

            # ==========================================================



            with left_column:



                st.subheader("🎯 Prediction Results")



                if prediction == "Yes":



                    st.error(

                        "⚠️ Customer is likely to churn."

                    )



                else:



                    st.success(

                        "✅ Customer is unlikely to churn."

                    )



                st.metric(

                    "Prediction",

                    prediction

                )



                st.metric(

                    "Churn Probability",

                    format_probability(probability)

                )



                st.metric(

                    "Model Confidence",

                    format_confidence(confidence)

                )



                st.metric(

                    "Risk Level",

                    get_risk_level(probability)

                )



                st.progress(float(probability))



                st.caption(

                    f"Prediction generated on {timestamp}"

                )



            # ==========================================================

            # Right Column - Prediction Summary

            # ==========================================================



            with right_column:



                st.subheader("📋 Prediction Summary")



                st.info(summary)



                st.subheader("🧠 Prediction Insights")



                for insight in insights:



                    st.write(insight)



            st.divider()



            # ==========================================================

            # Customer Information

            # ==========================================================



            st.subheader("👤 Customer Information")



            with st.expander(

                "View Customer Details",

                expanded=False

            ):



                st.dataframe(

                    display_customer_data(customer),

                    use_container_width=True

                )



            st.divider()



            # ==========================================================

            # Download Prediction Report

            # ==========================================================



            st.download_button(

                label="📥 Download Prediction Report",

                data=report,

                file_name="customer_prediction_report.csv",

                mime="text/csv",

                use_container_width=True

            )



        except Exception as e:



            st.error(

                "Prediction failed."

            )



            st.exception(e)



# ==========================================================

# Footer

# ==========================================================



st.divider()



footer_left, footer_middle, footer_right = st.columns(3)



footer_left.metric(

    "Model",

    "XGBoost"

)



footer_middle.metric(

    "Dataset",

    "Telco Customer Churn"

)



footer_right.metric(

    "Version",

    "2.0"

)



st.caption(

    """

Built with ❤️ using Streamlit, Scikit-learn and XGBoost.



Author: Palmer Ogiriki

"""

)