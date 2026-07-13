"""
SHAP Explainability Utilities
=============================

This module provides helper functions for explaining machine learning
models using SHAP.

Author: Palmer Ogiriki
Project: Customer Churn Prediction System
"""

import shap
import matplotlib.pyplot as plt
import os


def plot_shap_summary(model, X_train):
    """
    Generate and save a SHAP summary plot.

    Parameters
    ----------
    model : Trained XGBoost model
        The fitted machine learning model.

    X_train : pandas.DataFrame
        Training data used to compute SHAP values.

    Returns
    -------
    None
    """

    explainer = shap.TreeExplainer(model)

    shap_values = explainer.shap_values(X_train)

    os.makedirs("../reports/figures", exist_ok=True)

    shap.summary_plot(
        shap_values,
        X_train,
        show=False
    )

    plt.tight_layout()

    plt.savefig(
        "../reports/figures/shap_summary.png",
        dpi=300
    )

    plt.show()