# Functional Requirement Document (FRD)

## Functional Requirements

### Data Ingestion

- Load cloud usage data into Google Cloud Storage.
- Import data into BigQuery Bronze Layer.

---

### Data Transformation

- Clean raw cloud usage data.
- Convert timestamps.
- Validate data quality.
- Create Silver Layer.
- Build Gold analytical tables.

---

### AI Module

- Load processed data.
- Perform feature engineering.
- Detect anomalies using Isolation Forest.
- Generate anomaly scores.
- Generate optimization recommendations.

---

### Analytics

- Calculate cloud cost KPIs.
- Generate monthly cost trends.
- Analyze regional cloud usage.
- Analyze service-wise cloud spending.
- Identify inefficient resources.

---

### Reporting

- Power BI dashboards.
- Streamlit dashboard.
- Export AI predictions to BigQuery.
- Export prediction results to CSV.

---

## Non-Functional Requirements

- Modular architecture
- Scalable data pipeline
- Cloud-native implementation
- Reusable SQL scripts
- Production-ready Python code


# Cloud Cost Forecasting

## Objective

Predict future cloud spending using historical cloud usage data.

---

## Business Purpose

Cloud cost forecasting helps organizations:

- Estimate future cloud expenses.
- Plan infrastructure budgets.
- Identify increasing cost trends.
- Support financial planning.

---

## Planned Approach

Historical cloud cost data will be used to train forecasting models.

Potential algorithms include:

- Prophet
- Linear Regression

---

## Future Scope

Future versions of the platform will include:

- Monthly cloud cost forecasting
- Budget prediction
- Cost trend visualization
- Forecast accuracy measurement