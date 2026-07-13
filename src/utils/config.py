"""
Project Configuration
=====================

This module stores all common paths used throughout the project.

Author: Palmer Ogiriki
Project: Customer Churn Prediction System
"""

from pathlib import Path

# ===============================
# Project Root
# ===============================
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# ===============================
# Data Directories
# ===============================
DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

# ===============================
# Models Directory
# ===============================
MODELS_DIR = PROJECT_ROOT / "models"

# ===============================
# Reports Directory
# ===============================
REPORTS_DIR = PROJECT_ROOT / "reports"

FIGURES_DIR = REPORTS_DIR / "figures"