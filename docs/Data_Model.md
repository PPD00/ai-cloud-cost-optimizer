# Data Model Design

## Project Name

AI-Based Cloud Cost Optimizer

---

# 1. Data Warehouse Architecture

The project follows a Medallion Architecture (Bronze, Silver, Gold) to ensure data quality, scalability, and maintainability.

```text
Source CSV
    │
    ▼
Bronze Layer (Raw Data)
    │
    ▼
Silver Layer (Cleaned & Standardized Data)
    │
    ▼
Gold Layer (Business-Ready Data)
    │
    ├── Power BI Dashboard
    └── Python Forecasting & Optimization
```

This architecture separates raw ingestion, data transformation, and business reporting layers.

---

# 2. Bronze Layer Design

## Purpose

Store raw source data exactly as received from the source system without any transformations.

## Table

bronze_cloud_usage

## Characteristics

* Raw cloud billing and usage data.
* Original column names retained.
* No cleansing or validation applied.
* Serves as the system of record.

## Source

cloud_billing_usage.csv

---

# 3. Silver Layer Design

## Purpose

Clean, standardize, and enrich raw data for analytical processing.

## Table

silver_cloud_usage

## Transformations

* Standardize data types.
* Convert date fields into TIMESTAMP format.
* Validate cost and utilization fields.
* Remove duplicate records.
* Standardize region names.
* Create derived date attributes.
* Calculate usage duration.

## Output

Analytics-ready dataset with consistent and validated data.

---

# 4. Gold Layer Design

## Purpose

Provide business-ready datasets optimized for reporting, KPI calculations, optimization analysis, and forecasting.

## Tables

### gold_cost_summary

Contains service-level and region-level cost metrics.

### gold_resource_efficiency

Contains utilization and efficiency metrics for resources.

### gold_optimization_candidates

Contains optimization recommendations and estimated savings.

### gold_forecast_input

Contains historical cost metrics used for forecasting models.

---

# 5. Fact Table Design

## Table Name

fact_cloud_usage

## Purpose

Store measurable cloud usage and cost events.

## Measures

* Usage Quantity
* CPU Utilization (%)
* Memory Utilization (%)
* Network Inbound Data
* Network Outbound Data
* Cost Per Quantity
* Unrounded Cost
* Rounded Cost
* Total Cost (INR)

## Grain

One row represents one resource usage event for a specific usage period.

---

# 6. Dimension Table Design

## dim_service

Stores cloud service information.

### Columns

* service_key
* service_name

---

## dim_region

Stores region information.

### Columns

* region_key
* region_name

---

## dim_date

Stores calendar attributes for reporting and trend analysis.

### Columns

* date_key
* date
* month
* quarter
* year

---

# 7. Grain Definition

The grain of the fact table is:

> One Resource × One Usage Period

Each record represents a single resource consumption event captured within a specific start and end usage window.

Defining the grain ensures consistent aggregations and KPI calculations throughout the project.

---

# 8. Star Schema

The warehouse follows a Star Schema design.

```text
                 dim_service
                        │
                        │
dim_region ─── fact_cloud_usage ─── dim_date
```

## Benefits

* Simplified reporting.
* Faster query performance.
* Easy integration with Power BI.
* Industry-standard analytical model.

---

# 9. Partitioning Strategy

## Partition Column

usage_date

## Purpose

Partitioning reduces the amount of data scanned during query execution.

## Benefits

* Improved query performance.
* Reduced BigQuery query costs.
* Better scalability for large datasets.

---

# 10. Clustering Strategy

## Cluster Columns

* service_name
* region

## Purpose

Cluster frequently queried columns to improve query efficiency.

## Benefits

* Faster filtering operations.
* Lower query processing costs.
* Improved dashboard performance.

---

# Data Model Summary

The solution uses a Medallion Architecture with Bronze, Silver, and Gold layers. Data is modeled using a Star Schema consisting of one fact table and multiple dimension tables. The architecture supports cloud cost analytics, resource utilization analysis, optimization recommendations, and forecasting while ensuring scalability, maintainability, and efficient query performance in BigQuery.
