# Data Profiling Document

## Project Name

AI-Based Cloud Cost Optimizer

---

# 1. Purpose of Data Profiling

Data profiling is the process of understanding the structure, quality, content, and business meaning of the dataset before designing data models, writing SQL queries, or building dashboards.

The objective of this phase is to:

* Understand the dataset structure.
* Identify dimensions and measures.
* Understand business meaning of each column.
* Detect potential data quality issues.
* Discover KPIs and analytical opportunities.
* Prepare the dataset for data modeling and reporting.

---

# 2. Dataset Overview

The dataset contains cloud resource usage, utilization, network traffic, and cost information generated from different cloud services.

The data can be used to:

* Analyze cloud spending.
* Identify high-cost services.
* Monitor resource utilization.
* Detect underutilized resources.
* Generate optimization recommendations.
* Forecast future cloud costs.

Each row represents the usage and cost information of a cloud resource during a specific usage period.

---

# 3. Sample Record

| Resource ID  | Service Name   | Usage Quantity | Usage Unit | Region        | CPU Utilization | Memory Utilization | Network Inbound | Network Outbound | Start Date       | End Date         | Cost Per Quantity | Unrounded Cost | Rounded Cost | Total Cost INR |
| ------------ | -------------- | -------------- | ---------- | ------------- | --------------- | ------------------ | --------------- | ---------------- | ---------------- | ---------------- | ----------------- | -------------- | ------------ | -------------- |
| res-ST6BAJ2N | Cloud Dataproc | 954.9843       | Requests   | europe-north1 | 92.72           | 70.42              | 77097035547     | 82685933273      | 01-08-2024 22:24 | 07-08-2024 06:54 | 5.24              | 5004.12        | 5004         | 415332         |

---

# 4. Column Analysis

## Resource ID

### Data Type

STRING

### Description

Unique identifier assigned to a cloud resource.

### Example

res-ST6BAJ2N

### Business Use

Used to uniquely identify resources and perform resource-level analysis.

### Possible Questions

* Which resources generate the highest cost?
* Which resources are underutilized?
* Which resources should be optimized?

---

## Service Name

### Data Type

STRING

### Description

Name of the cloud service generating the usage.

### Example

* BigQuery
* Cloud Dataproc
* Pub/Sub
* Cloud Spanner

### Business Use

Used to analyze cloud spending by service.

### Possible Questions

* Which service contributes the highest cost?
* Which service has the highest utilization?
* Which service has the highest growth in spending?

---

## Usage Quantity

### Data Type

FLOAT

### Description

Amount of resource consumed.

### Example

954.9843

### Business Use

Represents workload volume consumed by the service.

### Possible Questions

* Which services are most heavily used?
* How does usage impact cost?

---

## Usage Unit

### Data Type

STRING

### Description

Measurement unit of resource consumption.

### Examples

* GB
* Requests
* Hours

### Business Use

Provides context to usage quantity values.

---

## Region / Zone

### Data Type

STRING

### Description

Cloud region where the resource is deployed.

### Examples

* us-central1
* europe-west1
* asia-south1

### Business Use

Used for regional cost and utilization analysis.

### Possible Questions

* Which region is the most expensive?
* Which region consumes the most resources?

---

## CPU Utilization (%)

### Data Type

FLOAT

### Description

Percentage of CPU resources being utilized.

### Example

92.72

### Business Use

Important metric for resource optimization and rightsizing decisions.

### Possible Questions

* Which resources are overutilized?
* Which resources are underutilized?
* Can the resource size be reduced?

---

## Memory Utilization (%)

### Data Type

FLOAT

### Description

Percentage of memory being utilized.

### Example

70.42

### Business Use

Helps determine whether allocated memory is being effectively used.

### Possible Questions

* Are resources over-provisioned?
* Are resources consuming excessive memory?

---

## Network Inbound Data (Bytes)

### Data Type

INTEGER / BIGINT

### Description

Amount of incoming network traffic.

### Example

77097035547

### Business Use

Used to analyze incoming data traffic patterns.

---

## Network Outbound Data (Bytes)

### Data Type

INTEGER / BIGINT

### Description

Amount of outgoing network traffic.

### Example

82685933273

### Business Use

Used to analyze data transfer activity and network-related costs.

---

## Usage Start Date

### Data Type

TIMESTAMP

### Description

Start time of resource usage.

### Example

01-08-2024 22:24

### Business Use

Used for time-series analysis and trend reporting.

---

## Usage End Date

### Data Type

TIMESTAMP

### Description

End time of resource usage.

### Example

07-08-2024 06:54

### Business Use

Used to calculate usage duration and resource activity periods.

---

## Cost Per Quantity ($)

### Data Type

FLOAT

### Description

Cost charged per unit of resource consumption.

### Example

5.24

### Business Use

Helps understand pricing structure of cloud services.

---

## Unrounded Cost ($)

### Data Type

FLOAT

### Description

Actual calculated cloud cost before rounding.

### Example

5004.12

### Business Use

Used for precise financial calculations.

---

## Rounded Cost ($)

### Data Type

INTEGER

### Description

Rounded billing cost.

### Example

5004

### Business Use

Used for reporting and billing summaries.

---

## Total Cost (INR)

### Data Type

INTEGER

### Description

Final cost converted into Indian Rupees.

### Example

415332

### Business Use

Primary financial metric used throughout the project.

### Possible Questions

* What is total cloud spend?
* Which service costs the most?
* Which region generates the highest cost?

---

# 5. Dimension and Measure Classification

## Dimensions

Dimensions describe business entities and are used for filtering, grouping, and categorization.

* Resource ID
* Service Name
* Usage Unit
* Region / Zone
* Usage Start Date
* Usage End Date

---

## Measures

Measures are numerical values used for aggregation and KPI calculations.

* Usage Quantity
* CPU Utilization
* Memory Utilization
* Network Inbound Data
* Network Outbound Data
* Cost Per Quantity
* Unrounded Cost
* Rounded Cost
* Total Cost (INR)

---

# 6. Initial Data Quality Checks

The following validations should be performed before data modeling:

## Missing Values

Check for missing values in:

* Resource ID
* Service Name
* Region
* CPU Utilization
* Memory Utilization
* Cost Fields

---

## Duplicate Records

Check whether identical records appear multiple times.

---

## Invalid Utilization Values

CPU and Memory utilization should remain between:

0% and 100%

---

## Invalid Cost Values

Verify that:

* Costs are not negative.
* Costs are not unexpectedly zero.

---

## Date Validation

Ensure:

Usage Start Date < Usage End Date

for all records.

---

# 7. Business Opportunities Identified

Based on profiling, the following analytics opportunities were identified:

## Cost Analysis

* Cost by Service
* Cost by Region
* Monthly Spending Trends
* Top Costly Resources

---

## Utilization Analysis

* CPU Utilization Analysis
* Memory Utilization Analysis
* Resource Efficiency Monitoring

---

## Optimization Analysis

* Idle Resource Detection
* Underutilized Resource Detection
* Potential Cost Savings Estimation

---

## Forecasting Analysis

* Monthly Cost Forecasting
* Cost Growth Analysis
* Budget Planning Support

---

# 8. Preliminary KPIs Identified

### Total Cloud Cost

SUM(Total Cost INR)

---

### Average CPU Utilization

AVG(CPU Utilization)

---

### Average Memory Utilization

AVG(Memory Utilization)

---

### Cost by Service

SUM(Total Cost INR) GROUP BY Service Name

---

### Cost by Region

SUM(Total Cost INR) GROUP BY Region

---

### Underutilized Resources

CPU < 20%
AND
Memory < 30%

---

### Idle Resources

CPU < 5%

---

### Potential Savings

Estimated based on optimization recommendations.

---

### Forecasted Cloud Cost

Predicted future spending using historical usage and cost trends.

---

# Conclusion

The dataset provides sufficient information to build a Cloud Cost Optimization solution focused on cost analytics, resource utilization monitoring, optimization recommendations, and cloud cost forecasting. The dataset contains both operational and financial metrics that support the development of dashboards, KPIs, and decision-making insights for FinOps and Cloud Operations teams.
