"""
Feature importance utilities.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os


def plot_feature_importance(model, feature_names, top_n=15):
    """
    Plot and save feature importance.
    """

    importance = pd.DataFrame({
        "Feature": feature_names,
        "Importance": model.feature_importances_
    })

    importance = importance.sort_values(
        by="Importance",
        ascending=False
    )

    plt.figure(figsize=(12, 8))

    plt.barh(
        importance["Feature"][:top_n][::-1],
        importance["Importance"][:top_n][::-1]
    )

    plt.xlabel("Importance")
    plt.title("Top Feature Importance")

    plt.tight_layout()

    os.makedirs("../reports/figures", exist_ok=True)

    plt.savefig(
        "../reports/figures/feature_importance.png",
        dpi=300
    )

    plt.show()

    return importance