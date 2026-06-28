-- Data Quality Validation (before building gold data)

-- 1. Row count check
SELECT COUNT(*)
FROM bronze_dataset.bronze_cloud_usage;


SELECT COUNT(*)
FROM silver_dataset.silver_cloud_usage;

-- 2. Null check
SELECT
COUNT(*) AS total_rows,

COUNT(resource_id) AS resource_id_count,

COUNT(service_name) AS service_name_count,

COUNT(usage_start_ts) AS start_ts_count,

COUNT(usage_end_ts) AS end_ts_count

FROM silver_dataset.silver_cloud_usage;

-- 3. CPU Utilization Check
SELECT *
FROM silver_dataset.silver_cloud_usage
WHERE cpu_utilization_pct < 0
   OR cpu_utilization_pct > 100;


-- 4. Memory Utilization check
   SELECT *
FROM silver_dataset.silver_cloud_usage
WHERE memory_utilization_pct < 0
   OR memory_utilization_pct > 100;


-- 5. Cost Validation
   SELECT *
FROM silver_dataset.silver_cloud_usage
WHERE total_cost_inr < 0;

-- 6. Duration Validation
SELECT *
FROM silver_dataset.silver_cloud_usage
WHERE usage_duration_hours < 0;


-- 7. Duplication Resource Check
SELECT
resource_id,
COUNT(*) AS cnt
FROM silver_dataset.silver_cloud_usage
GROUP BY resource_id
HAVING COUNT(*) > 1;

-- 8. Service Distribution
SELECT
service_name,
COUNT(*) AS records
FROM silver_dataset.silver_cloud_usage
GROUP BY service_name
ORDER BY records DESC;