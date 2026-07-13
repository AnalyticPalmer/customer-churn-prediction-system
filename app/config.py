"""
Configuration File
==================

Central configuration for the Customer Churn Prediction System.

Author: Palmer Ogiriki
Version: 2.0
"""

from pathlib import Path

# ==========================================================
# Project Directories
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

MODELS_DIR = PROJECT_ROOT / "models"

DATA_DIR = PROJECT_ROOT / "data"

REPORTS_DIR = PROJECT_ROOT / "reports"

ASSETS_DIR = PROJECT_ROOT / "app" / "assets"

# ==========================================================
# Model Files
# ==========================================================

MODEL_FILE = MODELS_DIR / "best_xgboost.pkl"

PREPROCESSOR_FILE = MODELS_DIR / "preprocessor.pkl"

# ==========================================================
# Application Settings
# ==========================================================

APP_TITLE = "Customer Churn Prediction System"

APP_VERSION = "2.0"

MODEL_NAME = "XGBoost"

DATASET_NAME = "Telco Customer Churn"

FRAMEWORK = "Streamlit"

AUTHOR = "Palmer Ogiriki"

# ==========================================================
# Prediction Threshold
# ==========================================================

CHURN_THRESHOLD = 0.50