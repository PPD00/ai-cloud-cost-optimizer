"""
=========================================================
Feature Engineering Module
=========================================================

Purpose:
--------
Prepares cloud usage data for machine learning by
selecting relevant features, handling missing values,
and scaling numerical features.

Author : Priyanshu Prakash
Project: AI-Powered Cloud Governance &
         Cost Optimization Platform
"""

import logging
import pandas as pd

from sklearn.preprocessing import StandardScaler

from config.config import FEATURE_COLUMNS

# ==========================================================
# Configure Logger
# ==========================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


# ==========================================================
# Handle Missing Values
# ==========================================================

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fill missing values in feature columns using median.

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
    """

    logger.info("Handling missing values...")

    for column in FEATURE_COLUMNS:

        df[column] = df[column].fillna(df[column].median())

    return df


# ==========================================================
# Select ML Features
# ==========================================================

def select_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Select only ML feature columns.

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
    """

    logger.info("Selecting ML features...")

    return df[FEATURE_COLUMNS].copy()


# ==========================================================
# Scale Features
# ==========================================================

def scale_features(feature_df: pd.DataFrame):
    """
    Standardize numerical features.

    Parameters
    ----------
    feature_df : pd.DataFrame

    Returns
    -------
    scaled_features : ndarray
    scaler : StandardScaler
    """

    logger.info("Scaling features...")

    scaler = StandardScaler()

    scaled_features = scaler.fit_transform(feature_df)

    logger.info("Feature scaling completed.")

    return scaled_features, scaler


# ==========================================================
# Complete Feature Engineering Pipeline
# ==========================================================

def prepare_features(df: pd.DataFrame):
    """
    Complete feature engineering pipeline.

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    processed_df : pd.DataFrame
    scaled_features : ndarray
    scaler : StandardScaler
    """

    logger.info("Starting feature engineering...")

    processed_df = handle_missing_values(df)

    feature_df = select_features(processed_df)

    scaled_features, scaler = scale_features(feature_df)

    logger.info("Feature engineering completed successfully.")

    return processed_df, scaled_features, scaler