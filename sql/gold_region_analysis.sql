CREATE OR REPLACE TABLE gold_dataset.gold_region_analysis AS

SELECT

    region_zone,

    ROUND(SUM(total_cost_inr),2) AS total_cost_inr,

    ROUND(AVG(total_cost_inr),2) AS avg_cost_inr,

    COUNT(resource_id) AS resource_count,

    ROUND(AVG(cpu_utilization_pct),2)
        AS avg_cpu_utilization,

    ROUND(AVG(memory_utilization_pct),2)
        AS avg_memory_utilization

FROM silver_dataset.silver_cloud_usage

GROUP BY region_zone

ORDER BY total_cost_inr DESC;