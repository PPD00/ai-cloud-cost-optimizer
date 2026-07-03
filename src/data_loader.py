"""
=========================================================
Data Loader Module
=========================================================

Purpose:
--------
Loads cloud usage data from BigQuery and returns a
Pandas DataFrame.

Author : Priyanshu Prakash
Project: AI-Powered Cloud Governance &
         Cost Optimization Platform
"""

import logging
import pandas as pd
from google.cloud import bigquery

from config.config import (
    PROJECT_ID,
    SILVER_TABLE
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
# Create BigQuery Client
# ==========================================================

def create_bigquery_client() -> bigquery.Client:
    """
    Creates and returns a BigQuery client.

    Returns
    -------
    bigquery.Client
        Authenticated BigQuery client.
    """

    try:

        client = bigquery.Client(project=PROJECT_ID)

        logger.info("BigQuery client created successfully.")

        return client

    except Exception as error:

        logger.error(f"Unable to create BigQuery client : {error}")

        raise


# ==========================================================
# Load Data
# ==========================================================

def load_cloud_usage_data() -> pd.DataFrame:
    """
    Loads cloud usage data from the Silver table.

    Returns
    -------
    pd.DataFrame
        Cloud usage dataframe.
    """

    try:

        client = create_bigquery_client()

        query = f"""
        SELECT *
        FROM `{SILVER_TABLE}`
        """

        logger.info("Executing BigQuery SQL...")

        dataframe = client.query(query).to_dataframe()

        logger.info(
            f"Successfully loaded {len(dataframe)} records."
        )

        return dataframe

    except Exception as error:

        logger.error(
            f"Error while loading data : {error}"
        )

        raise


# ==========================================================
# Test Module
# ==========================================================

if __name__ == "__main__":

    df = load_cloud_usage_data()

    print(df.head())