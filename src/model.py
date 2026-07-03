"""
=========================================================
Machine Learning Model Module
=========================================================

Purpose:
--------
Train, save, load, and use an Isolation Forest model
for anomaly detection on cloud resource usage.

Author : Priyanshu Prakash
Project: AI-Powered Cloud Governance &
         Cost Optimization Platform
"""

import logging
import joblib
import numpy as np

from sklearn.ensemble import IsolationForest

from config.config import (
    MODEL_NAME,
    MODEL_PATH,
    N_ESTIMATORS,
    CONTAMINATION,
    RANDOM_STATE
)

# ==========================================================
# Configure Logger
# ==========================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


# ==========================================================
# Train Model
# ==========================================================

def train_model(features):
    """
    Train Isolation Forest model.

    Parameters
    ----------
    features : ndarray

    Returns
    -------
    IsolationForest
    """

    logger.info(f"Training {MODEL_NAME} model...")

    model = IsolationForest(

        n_estimators=N_ESTIMATORS,

        contamination=CONTAMINATION,

        random_state=RANDOM_STATE

    )

    model.fit(features)

    logger.info("Model training completed.")

    return model


# ==========================================================
# Predict Anomalies
# ==========================================================

def predict_anomalies(model, features):
    """
    Predict anomalies.

    Returns
    -------
    predictions
    """

    logger.info("Generating anomaly predictions...")

    predictions = model.predict(features)

    return predictions


# ==========================================================
# Calculate Anomaly Scores
# ==========================================================

def calculate_anomaly_scores(model, features):
    """
    Calculate anomaly scores.

    Returns
    -------
    ndarray
    """

    logger.info("Calculating anomaly scores...")

    scores = model.decision_function(features)

    return scores


# ==========================================================
# Save Model
# ==========================================================

def save_model(model):
    """
    Save trained model.
    """

    joblib.dump(model, MODEL_PATH)

    logger.info(f"Model saved to {MODEL_PATH}")


# ==========================================================
# Load Model
# ==========================================================

def load_model():
    """
    Load saved model.
    """

    logger.info("Loading trained model...")

    model = joblib.load(MODEL_PATH)

    return model


# ==========================================================
# Complete Training Pipeline
# ==========================================================

def train_pipeline(features):
    """
    Complete ML training pipeline.
    """

    model = train_model(features)

    predictions = predict_anomalies(
        model,
        features
    )

    scores = calculate_anomaly_scores(
        model,
        features
    )

    save_model(model)

    logger.info("Training pipeline completed.")

    return model, predictions, scores