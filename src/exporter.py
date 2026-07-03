"""
=========================================================
Exporter Module
=========================================================

Purpose:
--------
Exports AI prediction results to CSV and BigQuery.

Author : Priyanshu Prakash
Project : AI-Powered Cloud Governance &
          Cost Optimization Platform
"""

import logging
import pandas as pd

from google.cloud import bigquery

from config.config import (
    PROJECT_ID,
    AI_TABLE,
    OUTPUT_CSV
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
# Export CSV
# ==========================================================

def export_to_csv(df: pd.DataFrame):
    """
    Export prediction results to CSV.
    """

    try:

        df.to_csv(
            OUTPUT_CSV,
            index=False
        )

        logger.info(
            f"CSV exported successfully : {OUTPUT_CSV}"
        )

    except Exception as error:

        logger.error(error)

        raise


# ==========================================================
# Export to BigQuery
# ==========================================================


def export_to_bigquery(df: pd.DataFrame):
    """
    Upload AI prediction results to BigQuery.
    """

    try:

        client = bigquery.Client(project=PROJECT_ID)

        # -----------------------------------------
        # Select only required columns
        # -----------------------------------------

        prediction_df = df[
            [
                "resource_id",
                "service_name",
                "region_zone",
                "usage_date",
                "cpu_utilization_pct",
                "memory_utilization_pct",
                "usage_duration_hours",
                "total_cost_inr",
                "anomaly_flag",
                "anomaly_score",
                "severity",
                "recommendation"
            ]
        ].copy()

        job_config = bigquery.LoadJobConfig(

            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,

            autodetect=True

        )

        job = client.load_table_from_dataframe(

            prediction_df,

            AI_TABLE,

            job_config=job_config

        )

        job.result()

        logger.info(
            f"AI predictions uploaded successfully to {AI_TABLE}"
        )

    except Exception as error:

        logger.error(error)

        raise


# ==========================================================
# Complete Export Pipeline
# ==========================================================

def export_results(df: pd.DataFrame):
    """
    Export all prediction results.
    """

    logger.info(
        "Starting export pipeline..."
    )

    export_to_csv(df)

    export_to_bigquery(df)

    logger.info(
        "Export pipeline completed."
    )