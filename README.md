# Snowflake 30-Day Admin Mastery Plan

**For Oracle/SQL Server DBAs → Snowflake Admin**  
*By Ravi Boppudi | 20+ Years Experience | UK Focus*  

This repo is your **hands-on roadmap** to Snowflake Admin proficiency in 30 days. Includes scripts, dashboards, and cert prep. Goal: SnowPro Core Certified + Portfolio for £120K+ roles.

## Prerequisites
- Snowflake Trial: [snowflake.com/trial](https://snowflake.com/trial)
- Tools: Snowsight, SnowSQL, VS Code + Snowflake Extension
- Sample Data: `SNOWFLAKE_SAMPLE_DATA`

## 30-Day Plan Overview

### Week 1: Core Concepts & Setup

| Day | Focus | Task | Script / Command |
|-----|-------|------|------------------|
| **1** | Account & UI | Sign up, explore Snowsight, create `DEV_WH` | `CREATE WAREHOUSE DEV_WH WAREHOUSE_SIZE=XSMALL AUTO_SUSPEND=60;` |
| **2** | SQL Basics | Load sample data, run queries | `USE DATABASE SNOWFLAKE_SAMPLE_DATA; SELECT * FROM TPCDS_SF100TCL.WEB_SITE LIMIT 5;` |
| **3** | Storage vs Compute | Create `STAGING_DB`, `PROD_DB` | `CREATE TRANSIENT DATABASE STAGING_DB;` |
| **4** | Virtual Warehouses | Scale `DEV_WH` → `LARGE`, test cost | `ALTER WAREHOUSE DEV_WH SET WAREHOUSE_SIZE = LARGE;` |
| **5** | Roles & Users | Create `DBA_KUMAR`, `ANALYST_UK` | See `scripts/rbac_setup.sql` |
| **6** | Access Control | Grant `SELECT` on `PROD_DB` | `GRANT USAGE ON DATABASE PROD_DB TO ROLE ANALYST_UK;` |
| **7** | **Quiz** | Share a query result with `ANALYST_UK` | N/A |

### Week 2: Data Loading & ETL

| Day | Focus | Task | Script |
|-----|-------|------|--------|
| **8** | Stages | Create internal stage | `CREATE STAGE STAGING_DB.PUBLIC.MY_STAGE;` |
| **9** | Snowpipe | Auto-ingest CSV from S3 | See `scripts/etl_pipeline.sql` |
| **10** | Tasks | Schedule daily refresh | See `scripts/etl_pipeline.sql` |
| **11** | Streams | CDC on `SALES` table | `CREATE STREAM SALES_STREAM ON TABLE SALES;` |
| **12** | Zero-Copy Clone | Clone `PROD_DB` for testing | `CREATE DATABASE TEST_DB CLONE PROD_DB;` |
| **13** | Time Travel | Recover dropped table | `UNDROP TABLE SALES;` |
| **14** | **Project** | Build ETL pipeline: S3 → Stage → Pipe → Task → Stream | Run `scripts/etl_pipeline.sql` |

### Week 3: Performance, Cost & Security

| Day | Focus | Task | Script |
|-----|-------|------|--------|
| **15** | Query History | Find top 5 credit-burning queries | See `scripts/daily_cost_report.sql` |
| **16** | Clustering Keys | Fix slow `JOIN` on `ORDER_DATE` | `ALTER TABLE SALES CLUSTER BY (ORDER_DATE);` |
| **17** | Materialized Views | Speed up dashboard | `CREATE MATERIALIZED VIEW MV_DAILY_SALES AS SELECT DATE, SUM(AMOUNT) FROM SALES GROUP BY DATE;` |
| **18** | Cost Control | Set resource monitor | `CREATE RESOURCE MONITOR FINANCE_LIMIT WITH CREDIT_QUOTA=500 FREQUENCY=MONTHLY;` |
| **19** | Dynamic Data Masking | Hide PII | `CREATE MASKING POLICY EMAIL_MASK AS (val STRING) RETURNS STRING -> CASE WHEN CURRENT_ROLE() IN ('ANALYST_UK') THEN SHA2(val) ELSE val END;` |
| **20** | Row Access Policy | Restrict by region | `CREATE ROW ACCESS POLICY RAP_UK AS (region VARCHAR) RETURNS BOOLEAN -> CURRENT_ROLE() IN ('DBA_KUMAR') OR region = 'UK';` |
| **21** | **Quiz** | Explain why `CLUSTER BY` ≠ index | N/A |

### Week 4: Automation, DR & Certification

| Day | Focus | Task | Script / Action |
|-----|-------|------|-----------------|
| **22** | Python + Snowflake | Auto-scale warehouse | Run `scripts/auto_scale.py` |
| **23** | Replication | Failover to `AWS_EU_WEST_2` | `ALTER DATABASE PROD_DB ENABLE REPLICATION TO ACCOUNTS AWS_EU_WEST_2;` |
| **24** | Failover Test | Switch primary | `ALTER DATABASE PROD_DB FAILOVER TO ACCOUNT AWS_EU_WEST_2;` |
| **25** | SnowPro Core Prep | Take 2 practice exams | See `cert_prep/practice_questions.md` |
| **26** | Portfolio Project | "Cost-Saving Dashboard" in Snowsight | Import `dashboards/cost_saving_dashboard.json` |
| **27** | Tags & Chargeback | Tag all warehouses | `ALTER WAREHOUSE SET TAG (COST_CENTER = 'FINANCE');` |
| **28** | Automation Script | Daily cost email | `CALL SYSTEM$SEND_EMAIL('cost_alert', 'dba@kumarbrk.co.uk', 'Daily Cost: £87', 'See attached report');` |
| **29** | Mock Interview | Answer: “How do you reduce Snowflake costs?” | Auto-suspend, clustering, resource monitors, query tuning |
| **30** | **CERTIFICATION DAY** | Book SnowPro Core Exam (£150) | [snowflake.com/certifications](https://www.snowflake.com/certifications/) |

## Usage
- Run SQL: `snowsql -f scripts/daily_cost_report.sql`
- Automate: `pip install -r requirements.txt && python scripts/auto_scale.py`
- Cert: Study `cert_prep/` → Book exam

## Portfolio Tips
- Deploy dashboard to Snowsight → Share link on LinkedIn
- Add to Resume: "Built ETL pipeline saving 20% compute costs"

**Contribute?** Fork & PR! 
