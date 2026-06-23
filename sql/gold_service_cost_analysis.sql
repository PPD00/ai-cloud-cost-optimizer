CREATE OR REPLACE TABLE gold_dataset.gold_service_cost_analysis AS

SELECT

    service_name,

    ROUND(SUM(total_cost_inr),2) AS total_cost_inr,

    ROUND(AVG(total_cost_inr),2) AS avg_cost_inr,

    COUNT(resource_id) AS resource_count,

    ROUND(AVG(cpu_utilization_pct),2)
        AS avg_cpu_utilization,

    ROUND(AVG(memory_utilization_pct),2)
        AS avg_memory_utilization

FROM silver_dataset.silver_cloud_usage

GROUP BY service_name

ORDER BY total_cost_inr DESC;