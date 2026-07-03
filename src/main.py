"""
=========================================================
Main Application
=========================================================

Purpose:
--------
Orchestrates the complete AI pipeline for the
AI-Powered Cloud Governance &
Cost Optimization Platform.

Author : Priyanshu Prakash
"""

import logging

from data_loader import load_cloud_usage_data
from feature_engineering import prepare_features
from model import train_pipeline
from recommendation_engine import apply_recommendations
from exporter import export_results


# ==========================================================
# Configure Logger
# ==========================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


# ==========================================================
# Main Pipeline
# ==========================================================

def run_pipeline():
    """
    Execute the complete AI pipeline.
    """

    logger.info("=" * 60)
    logger.info("Starting AI Cloud Cost Optimizer")
    logger.info("=" * 60)

    # --------------------------------------------------
    # Step 1 : Load Data
    # --------------------------------------------------

    df = load_cloud_usage_data()

    logger.info(f"Records Loaded : {len(df)}")

    # --------------------------------------------------
    # Step 2 : Feature Engineering
    # --------------------------------------------------

    processed_df, scaled_features, scaler = prepare_features(df)

    # --------------------------------------------------
    # Step 3 : Train Model
    # --------------------------------------------------

    model, predictions, scores = train_pipeline(
        scaled_features
    )

    # --------------------------------------------------
    # Step 4 : Store AI Results
    # --------------------------------------------------

    processed_df["anomaly_flag"] = predictions

    processed_df["anomaly_score"] = scores

    # --------------------------------------------------
    # Step 5 : Generate Recommendations
    # --------------------------------------------------

    processed_df = apply_recommendations(
        processed_df
    )

    # --------------------------------------------------
    # Step 6 : Export Results
    # --------------------------------------------------

    export_results(processed_df)

    logger.info("=" * 60)
    logger.info("Pipeline Completed Successfully")
    logger.info("=" * 60)


# ==========================================================
# Entry Point
# ==========================================================

if __name__ == "__main__":

    run_pipeline()