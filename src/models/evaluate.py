"""
Model evaluation utilities.
"""

import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    roc_auc_score
)


def evaluate_model(model, X_test, y_test):
    """
    Evaluate a trained classification model.
    """

    # Make predictions
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    # Convert numeric predictions (e.g., XGBoost) back to labels
    if y_pred.dtype != object:
        y_pred = pd.Series(y_pred).map({0: "No", 1: "Yes"})

    # Convert true labels to numeric for ROC-AUC
    y_test_numeric = y_test.map({"No": 0, "Yes": 1})

    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    auc = roc_auc_score(y_test_numeric, y_prob)

    print("=" * 50)
    print(f"Accuracy : {accuracy:.4f}")
    print(f"ROC-AUC  : {auc:.4f}")

    print("\nClassification Report")
    print(classification_report(y_test, y_pred))

    print("\nConfusion Matrix")
    print(confusion_matrix(y_test, y_pred))

    return accuracy, auc