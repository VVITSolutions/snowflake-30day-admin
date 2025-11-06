### SnowPro Advanced: Administrator (ADA-C01) Practice Questions (25 Total)

The SnowPro Advanced: Administrator certification validates expertise in advanced Snowflake administration, including account management, security/governance, performance tuning, data sharing, replication, and cost optimization. The exam has ~65 questions (multiple-choice/multiple-response), 120 minutes, and a passing score of 750/1000 (scaled). Prerequisite: SnowPro Core. Focus on scenario-based questions drawing from real-world admin tasks.

These 25 practice questions are curated based on the official exam guide domains (approximate weights: Account Management ~20%, Security & Governance ~25%, Performance & Optimization ~20%, Data Sharing & Replication ~20%, Billing & DR ~15%). Answers and explanations follow each section for self-study. Use with Snowflake docs and hands-on trial practice.

---

## **Account Management & Configuration (20%)**

1. **Which role is required to modify account-level parameters like `NETWORK_POLICY`?**  
   A: SYSADMIN  
   B: SECURITYADMIN  
   C: ACCOUNTADMIN (Correct)  
   D: ORGADMIN  
   *Explanation*: ACCOUNTADMIN has full privileges for account configuration; others are limited.

2. **What command enables multi-factor authentication (MFA) enforcement at the account level?**  
   A: `ALTER ACCOUNT SET ENFORCE_MFA = TRUE;` (Correct)  
   B: `ALTER USER SET MFA_ENFORCED = TRUE;`  
   C: `CREATE NETWORK POLICY MFA_POLICY;`  
   D: `GRANT SECURITYADMIN TO ROLE;`  
   *Explanation*: This sets account-wide MFA policy; user-level is separate.

3. **In a scenario where users report connection timeouts, what account parameter should you check first?**  
   A: `CLIENT_SESSION_KEEP_ALIVE`  
   B: `QUERY_TAG`  
   C: `STATEMENT_TIMEOUT_IN_SECONDS` (Correct)  
   D: `AUTO_SUSPEND`  
   *Explanation*: Controls max query runtime; adjust for network issues.

4. **How do you create a reader account for data sharing?**  
   A: `CREATE READER ACCOUNT reader_acct WITH ORG_NAME = 'myorg';` (Correct)  
   B: `CREATE DATABASE READER_DB;`  
   C: `ALTER ACCOUNT SET READER = TRUE;`  
   D: `GRANT USAGE ON ACCOUNT TO READER_ROLE;`  
   *Explanation*: Reader accounts are on-premises for secure sharing without compute.

5. **What is the impact of setting `ALLOW_CLIENT_CHANGE_WAREHOUSE = FALSE`?**  
   A: Users cannot switch warehouses mid-session (Correct)  
   B: Warehouses auto-scale down  
   C: All queries use the default warehouse  
   D: Compute credits are capped  
   *Explanation*: Enforces session consistency for governance.

---

## **Security & Data Governance (25%)**

6. **Which command applies a column-level masking policy to sensitive data?**  
   A: `ALTER TABLE customers MODIFY COLUMN email SET MASKING POLICY email_mask;` (Correct)  
   B: `CREATE VIEW customers WITH MASKING POLICY email_mask;`  
   C: `GRANT MASKING POLICY email_mask TO TABLE customers;`  
   D: `ALTER POLICY email_mask ON COLUMN email;`  
   *Explanation*: Directly attaches policy to column for dynamic redaction.

7. **In a row access policy, how do you restrict data based on current user role?**  
   A: `RETURNS BOOLEAN -> CURRENT_ROLE() IN ('ANALYST_UK')` (Correct)  
   B: `RETURNS ROW -> USER_ROLE = 'ANALYST_UK'`  
   C: `WHERE CURRENT_USER() = 'analyst@uk.com'`  
   D: `FILTER BY ROLE 'ANALYST_UK'`  
   *Explanation*: Uses `CURRENT_ROLE()` for RBAC enforcement.

8. **What feature prevents unauthorized data exfiltration via shares?**  
   A: Secure Data Sharing with `ALLOW_READER_CREATE_ACCOUNT = FALSE` (Correct)  
   B: External Tokenization  
   C: Tri-Secret Secure  
   D: Key Pair Authentication  
   *Explanation*: Limits reader account creation for controlled sharing.

9. **How do you audit failed login attempts across the account?**  
   A: `SELECT * FROM ACCOUNT_USAGE.LOGIN_HISTORY WHERE IS_SUCCESS = FALSE;` (Correct)  
   B: `SHOW GRANTS TO USER;`  
   C: `QUERY_HISTORY WHERE ERROR_CODE = 403;`  
   D: `INFORMATION_SCHEMA.AUDIT_LOG;`  
   *Explanation*: LOGIN_HISTORY tracks authentication events.

10. **What is required to enable SCIM-based identity federation?**  
    A: Integrate with Okta/SAML and set `ALLOW_IDP_INITIATED_LOGIN = TRUE` (Correct)  
    B: Use `CREATE USER WITH FEDERATED = TRUE;`  
    C: Grant ORGADMIN role  
    D: Configure `EXTERNAL_OAUTH` only  
    *Explanation*: Supports SSO for governance.

---

## **Performance & Optimization (20%)**

11. **To optimize a large table with frequent range scans on DATE, what should you apply?**  
    A: `ALTER TABLE sales CLUSTER BY (order_date);` (Correct)  
    B: `CREATE INDEX idx_date ON sales (order_date);`  
    C: `ALTER TABLE sales ADD SEARCH OPTIMIZATION ON (order_date);`  
    D: `CREATE MATERIALIZED VIEW mv_sales AS SELECT * FROM sales;`  
    *Explanation*: Clustering keys enable micro-partition pruning.

12. **What causes excessive queueing in a multi-cluster warehouse?**  
    A: `MAX_CONCURRENCY_LEVEL` set too low (Correct)  
    B: `AUTO_SUSPEND` too short  
    C: `WAREHOUSE_SIZE` too small  
    D: `SCALING_POLICY = ECONOMY`  
    *Explanation*: Limits concurrent queries; increase for high load.

13. **How do you identify queries spilling to remote disk?**  
    A: Query Profile shows "Spilling to Remote Disk" (Correct)  
    B: `SELECT * FROM QUERY_HISTORY WHERE BYTES_SPILLED_TO_LOCAL = 0;`  
    C: `WAREHOUSE_METERING_HISTORY` credits > expected  
    D: `RESULT_CACHE_HIT = FALSE`  
    *Explanation*: Profile visualizes spill metrics.

14. **When using search optimization service, what is the trade-off?**  
    A: Faster point lookups but higher storage costs (Correct)  
    B: Reduced compute credits  
    C: Automatic clustering  
    D: No impact on Time Travel  
    *Explanation*: Builds auxiliary structures for semi-structured queries.

15. **What command forces a materialized view refresh?**  
    A: `ALTER MATERIALIZED VIEW mv_sales REBUILD;` (Correct)  
    B: `CALL COMPLETE_MV(mv_sales);`  
    C: `ALTER TABLE base_table REFRESH MV;`  
    D: `SYSTEM$REBUILD_MV(mv_sales);`  
    *Explanation*: Triggers immediate rebuild for stale views.

---

## **Data Sharing, Replication & DR (20%)**

16. **How do you create a secure share for cross-account data access?**  
    A: `CREATE SHARE sales_share; GRANT SELECT ON sales TO SHARE sales_share; ALTER SHARE sales_share ADD ACCOUNTS 'reader_acct';` (Correct)  
    B: `CREATE DATABASE SHARED_SALES;`  
    C: `GRANT USAGE ON DATABASE TO READER_ACCOUNT;`  
    D: `COPY INTO @external_stage FROM sales;`  
    *Explanation*: Shares live data without copying.

17. **What enables database replication across regions?**  
    A: `ALTER DATABASE prod_db ENABLE REPLICATION TO ACCOUNT replica_acct;` (Correct)  
    B: `CREATE REPLICA DATABASE prod_replica OF prod_db;`  
    C: `ALTER ACCOUNT SET REPLICATION = TRUE;`  
    D: `GRANT REPLICATION ON DATABASE prod_db;`  
    *Explanation*: Sets up primary-replica for failover.

18. **In a failover scenario, what command promotes a replica to primary?**  
    A: `ALTER DATABASE prod_db FAILOVER TO REPLICA replica_acct;` (Correct)  
    B: `SWITCHOVER DATABASE prod_db TO replica_acct;`  
    C: `PROMOTE REPLICA prod_replica;`  
    D: `ALTER REPLICATION GROUP SET PRIMARY = replica_acct;`  
    *Explanation*: Initiates planned failover.

19. **What is the retention period for Fail-safe in Business Critical edition?**  
    A: 7 days (Correct)  
    B: 1 day  
    C: 90 days  
    D: 14 days  
    *Explanation*: Post-Time Travel recovery; longer in higher editions.

20. **How do you share a stream for CDC across accounts?**  
    A: Grant `SELECT` on stream in a share (Correct)  
    B: Replicate the stream object  
    C: Use `COPY GRANTS` on table  
    D: Export to external stage  
    *Explanation*: Streams are shareable for change data capture.

---

## **Billing, Cost Management & Administration (15%)**

21. **What triggers a resource monitor notification at 75% quota?**  
    A: `CREATE RESOURCE MONITOR rm_monthly WITH CREDIT_QUOTA=1000 TRIGGERS ON 75% DO NOTIFY;` (Correct)  
    B: `ALTER ACCOUNT SET ALERT_THRESHOLD = 75%;`  
    C: `SET MAX_CREDITS = 1000;`  
    D: `GRANT MONITOR ON ACCOUNT TO SYSADMIN;`  
    *Explanation*: Automates alerts for cost control.

22. **How do you tag warehouses for cost allocation?**  
    A: `ALTER WAREHOUSE finance_wh SET TAG (dept='finance', env='prod');` (Correct)  
    B: `CREATE TAG dept_tag = 'finance'; GRANT TAG dept_tag TO WAREHOUSE finance_wh;`  
    C: `ALTER ACCOUNT SET TAG finance_wh = 'dept:finance';`  
    D: `LABEL WAREHOUSE finance_wh AS finance;`  
    *Explanation*: Enables query-by-tag reporting.

23. **What view tracks credit usage by tag?**  
    A: `ACCOUNT_USAGE.TAG_REFERENCES` joined with `WAREHOUSE_METERING_HISTORY` (Correct)  
    B: `QUERY_HISTORY WHERE TAG_VALUE = 'finance';`  
    C: `RESOURCE_MONITORS`  
    D: `BILLING_HISTORY`  
    *Explanation*: Combines for chargeback analysis.

24. **In multi-account org, who manages billing?**  
    A: ORGADMIN (Correct)  
    B: ACCOUNTADMIN per account  
    C: SECURITYADMIN  
    D: SYSADMIN  
    *Explanation*: Centralizes org-wide cost oversight.

25. **What reduces costs during low-load periods?**  
    A: `SCALING_POLICY = STANDARD` with auto-suspend (Correct)  
    B: Set `MIN_CLUSTER_COUNT = 1`  
    C: Use transient tables only  
    D: Enable result caching globally  
    *Explanation*: Balances concurrency and idle suspension.

---

## **Answers Summary**
| Q# | Correct Answer |
|----|----------------|
| 1-5 | C, A, C, A, A |
| 6-10 | A, A, A, A, A |
| 11-15 | A, A, A, A, A |
| 16-20 | A, A, A, A, A |
| 21-25 | A, A, A, A, A |

**Pro Tips**: 
- Practice scenarios in a trial account (e.g., set up replication, apply policies).
- Resources: Snowflake Docs (docs.snowflake.com), Exam Guide (learn.snowflake.com), VMExam free samples, Medium prep articles.
- Aim for 80%+ on mocks; exam is $375 USD.
