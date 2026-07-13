"""
Application Styling
===================

Custom CSS for the Customer Churn Prediction System.

Author: Palmer Ogiriki
Version: 2.0
"""

# ==========================================================
# Imports
# ==========================================================

import streamlit as st


# ==========================================================
# Load CSS
# ==========================================================

def load_css():
    """
    Apply custom styling to the Streamlit application.
    """

    st.markdown(
        """
<style>

/* ======================================================
General
====================================================== */

html,
body,
[class*="css"] {
    font-family: "Segoe UI", sans-serif;
}

/* ======================================================
Main Container
====================================================== */

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    padding-left:2rem;
    padding-right:2rem;
}

/* ======================================================
Sidebar
====================================================== */

[data-testid="stSidebar"]{
    background-color:#F8F9FA;
}

/* ======================================================
Metric Cards
====================================================== */

[data-testid="metric-container"]{
    background-color:white;
    border:1px solid #E5E7EB;
    padding:20px;
    border-radius:12px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.08);
}

/* ======================================================
Buttons
====================================================== */

.stButton > button{

    width:100%;

    height:3em;

    border-radius:10px;

    border:none;

    font-weight:bold;

    background:#2563EB;

    color:white;
}

.stButton > button:hover{

    background:#1D4ED8;

    color:white;
}

/* ======================================================
Download Button
====================================================== */

.stDownloadButton > button{

    width:100%;

    height:3em;

    border-radius:10px;

    font-weight:bold;
}

/* ======================================================
DataFrame
====================================================== */

[data-testid="stDataFrame"]{

    border-radius:10px;

    border:1px solid #E5E7EB;
}

/* ======================================================
Success Box
====================================================== */

.stSuccess{

    border-radius:10px;
}

/* ======================================================
Error Box
====================================================== */

.stError{

    border-radius:10px;
}

/* ======================================================
Expander
====================================================== */

.streamlit-expanderHeader{

    font-weight:bold;

    font-size:16px;
}

/* ======================================================
Footer
====================================================== */

footer{

    visibility:hidden;
}

</style>
        """,
        unsafe_allow_html=True
    )