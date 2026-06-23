CREATE OR REPLACE TABLE gold_dataset.gold_resource_efficiency AS

SELECT

    resource_id,

    service_name,

    region_zone,

    total_cost_inr,

    cpu_utilization_pct,

    memory_utilization_pct,

    ROUND(
        (cpu_utilization_pct + memory_utilization_pct) / 2,
        2
    ) AS efficiency_score,

    CASE

        WHEN cpu_utilization_pct < 30
         AND memory_utilization_pct < 30

        THEN 'UNDERUTILIZED'

        WHEN cpu_utilization_pct > 85
          OR memory_utilization_pct > 85

        THEN 'OVERUTILIZED'

        ELSE 'OPTIMIZED'

    END AS optimization_status,

    CASE

        WHEN cpu_utilization_pct < 30
         AND memory_utilization_pct < 30

        THEN ROUND(total_cost_inr * 0.20,2)

        ELSE 0

    END AS potential_savings_inr,

    CASE

        WHEN cpu_utilization_pct < 30
         AND memory_utilization_pct < 30

        THEN 'Downsize Resource'

        WHEN cpu_utilization_pct > 85
          OR memory_utilization_pct > 85

        THEN 'Scale Resource'

        ELSE 'No Action Needed'

    END AS recommendation

FROM silver_dataset.silver_cloud_usage;