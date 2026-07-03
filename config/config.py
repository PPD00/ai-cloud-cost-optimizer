"""
=========================================================
Project Configuration File
AI-Powered Cloud Governance & Cost Optimization Platform
=========================================================

This file stores all project configuration values.
Do not hardcode these values anywhere else.
"""

# =========================================================
# Google Cloud Configuration
# =========================================================

PROJECT_ID = "YOUR_GCP_PROJECT_ID"

BRONZE_DATASET = "bronze_dataset"
SILVER_DATASET = "silver_dataset"
GOLD_DATASET = "gold_dataset"
AI_DATASET = "ai_dataset"

SOURCE_TABLE = "silver_cloud_usage"
OUTPUT_TABLE = "ai_predictions"

# =========================================================
# BigQuery Table Names
# =========================================================

BRONZE_TABLE = f"{PROJECT_ID}.{BRONZE_DATASET}.bronze_cloud_usage"

SILVER_TABLE = f"{PROJECT_ID}.{SILVER_DATASET}.silver_cloud_usage"

GOLD_SERVICE_COST_TABLE = (
    f"{PROJECT_ID}.{GOLD_DATASET}.gold_service_cost"
)

GOLD_REGION_COST_TABLE = (
    f"{PROJECT_ID}.{GOLD_DATASET}.gold_region_cost"
)

GOLD_MONTHLY_COST_TABLE = (
    f"{PROJECT_ID}.{GOLD_DATASET}.gold_monthly_cost_trend"
)

AI_TABLE = (
    f"{PROJECT_ID}.{AI_DATASET}.{OUTPUT_TABLE}"
)

# =========================================================
# Model Configuration
# =========================================================

MODEL_NAME = "Isolation Forest"

N_ESTIMATORS = 100

CONTAMINATION = 0.05

RANDOM_STATE = 42

# =========================================================
# File Paths
# =========================================================

MODEL_PATH = "models/isolation_forest.pkl"

OUTPUT_CSV = "outputs/ai_predictions.csv"

LOG_FILE = "outputs/application.log"

# =========================================================
# Feature Columns Used By ML Model
# =========================================================

FEATURE_COLUMNS = [

    "cpu_utilization_pct",

    "memory_utilization_pct",

    "network_inbound_bytes",

    "network_outbound_bytes",

    "usage_duration_hours",

    "total_cost_inr"

]

# =========================================================
# Recommendation Thresholds
# =========================================================

LOW_CPU = 20

HIGH_CPU = 85

LOW_MEMORY = 30

HIGH_MEMORY = 85

LONG_RUNTIME = 120

HIGH_NETWORK = 80000000000

# =========================================================
# Severity Thresholds
# =========================================================

HIGH_SEVERITY = -0.20

MEDIUM_SEVERITY = -0.05


# ==============================================
# AI DATASET
# ==============================================

AI_DATASET = "ai_dataset"

AI_TABLE = f"{PROJECT_ID}.{AI_DATASET}.ai_predictions"