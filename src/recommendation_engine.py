"""
=========================================================
Recommendation Engine Module
=========================================================

Purpose:
--------
Generate business recommendations and severity levels
based on AI anomaly detection results.

Author : Priyanshu Prakash
Project: AI-Powered Cloud Governance &
         Cost Optimization Platform
"""

import logging

from config.config import (
    LOW_CPU,
    HIGH_CPU,
    LOW_MEMORY,
    HIGH_MEMORY,
    HIGH_NETWORK,
    LONG_RUNTIME,
    HIGH_SEVERITY,
    MEDIUM_SEVERITY
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
# Recommendation Logic
# ==========================================================

def generate_recommendation(row):
    """
    Generate business recommendation based on
    anomaly detection and resource utilization.
    """

    # ------------------------------------------
    # Normal Resource
    # ------------------------------------------

    if row["anomaly_flag"] == 1:

        return "No action required"

    # ------------------------------------------
    # Underutilized Resource
    # ------------------------------------------

    if (
        row["cpu_utilization_pct"] < LOW_CPU
        and row["memory_utilization_pct"] < LOW_MEMORY
    ):

        return "Downsize or terminate underutilized resource"

    # ------------------------------------------
    # Overutilized Resource
    # ------------------------------------------

    elif (
        row["cpu_utilization_pct"] > HIGH_CPU
        and row["memory_utilization_pct"] > HIGH_MEMORY
    ):

        return "Upgrade resource configuration"

    # ------------------------------------------
    # High Network Usage
    # ------------------------------------------

    elif row["network_outbound_bytes"] > HIGH_NETWORK:

        return "Investigate abnormal outbound network traffic"

    # ------------------------------------------
    # Long Running Resource
    # ------------------------------------------

    elif row["usage_duration_hours"] > LONG_RUNTIME:

        return "Review long-running workload"

    # ------------------------------------------
    # Unknown Anomaly
    # ------------------------------------------

    else:

        return "Manual investigation recommended"


# ==========================================================
# Severity Logic
# ==========================================================

def calculate_severity(score):
    """
    Assign severity level using anomaly score.
    """

    if score <= HIGH_SEVERITY:

        return "High"

    elif score <= MEDIUM_SEVERITY:

        return "Medium"

    else:

        return "Low"


# ==========================================================
# Apply Recommendation Engine
# ==========================================================

def apply_recommendations(df):
    """
    Apply recommendations and severity levels.
    """

    logger.info("Generating AI recommendations...")

    df["recommendation"] = df.apply(
        generate_recommendation,
        axis=1
    )

    df["severity"] = df["anomaly_score"].apply(
        calculate_severity
    )

    logger.info("Recommendation generation completed.")

    return df