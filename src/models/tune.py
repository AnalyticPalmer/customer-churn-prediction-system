"""
Hyperparameter tuning utilities.
"""

from sklearn.model_selection import RandomizedSearchCV
from xgboost import XGBClassifier


def tune_xgboost(X_train, y_train):
    """
    Tune an XGBoost model using RandomizedSearchCV.
    """

    y_train = y_train.map({"No": 0, "Yes": 1})

    model = XGBClassifier(
        random_state=42,
        eval_metric="logloss"
    )

    param_grid = {
        "n_estimators": [100, 200, 300],
        "max_depth": [3, 5, 7],
        "learning_rate": [0.01, 0.05, 0.1],
        "subsample": [0.8, 1.0],
        "colsample_bytree": [0.8, 1.0]
    }

    search = RandomizedSearchCV(
        estimator=model,
        param_distributions=param_grid,
        n_iter=10,
        cv=5,
        scoring="roc_auc",
        random_state=42,
        n_jobs=-1
    )

    search.fit(X_train, y_train)

    return search.best_estimator_, search.best_params_