"""
Preprocessing pipeline for the Customer Churn Prediction System.
"""

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def create_preprocessor(numerical_features, categorical_features):
    """
    Create a preprocessing pipeline.

    Parameters
    ----------
    numerical_features : list
        List of numerical column names.

    categorical_features : list
        List of categorical column names.

    Returns
    -------
    ColumnTransformer
        Configured preprocessing pipeline.
    """

    # Numerical pipeline
    numerical_pipeline = Pipeline(
        steps=[
            ("scaler", StandardScaler())
        ]
    )

    # Categorical pipeline
    categorical_pipeline = Pipeline(
        steps=[
            ("encoder", OneHotEncoder(handle_unknown="ignore"))
        ]
    )

    # Combine pipelines
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numerical_pipeline, numerical_features),
            ("cat", categorical_pipeline, categorical_features)
        ]
    )

    return preprocessor