CREATE OR REPLACE TABLE gold_dataset.gold_monthly_cost_trend AS

SELECT

    year,

    month,

    ROUND(SUM(total_cost_inr),2)
        AS total_cost_inr,

    ROUND(AVG(cpu_utilization_pct),2)
        AS avg_cpu_utilization,

    ROUND(AVG(memory_utilization_pct),2)
        AS avg_memory_utilization,

    COUNT(DISTINCT resource_id)
        AS total_resources

FROM silver_dataset.silver_cloud_usage

GROUP BY
    year,
    month

ORDER BY
    year,
    month;