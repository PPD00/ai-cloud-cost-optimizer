CREATE OR REPLACE TABLE silver_dataset.silver_cloud_usage AS

WITH base AS (
    SELECT
        *,
        PARSE_TIMESTAMP('%d-%m-%Y %H:%M', usage_start_date) AS start_ts,
        PARSE_TIMESTAMP('%d-%m-%Y %H:%M', usage_end_date) AS end_ts
    FROM bronze_dataset.bronze_cloud_usage
)

SELECT

    resource_id,
    service_name,
    usage_quantity,
    usage_unit,
    region_zone,

    cpu_utilization_pct,
    memory_utilization_pct,

    CAST(ROUND(network_inbound_bytes) AS INT64) AS network_inbound_bytes,
    CAST(ROUND(network_outbound_bytes) AS INT64) AS network_outbound_bytes,

    start_ts AS usage_start_ts,
    end_ts AS usage_end_ts,

    TIMESTAMP_DIFF(end_ts, start_ts, HOUR) AS usage_duration_hours,

    DATE(start_ts) AS usage_date,

    EXTRACT(MONTH FROM start_ts) AS month,
    EXTRACT(QUARTER FROM start_ts) AS quarter,
    EXTRACT(YEAR FROM start_ts) AS year,

    cost_per_quantity_usd,
    unrounded_cost_usd,
    rounded_cost_usd,
    total_cost_inr

FROM base;