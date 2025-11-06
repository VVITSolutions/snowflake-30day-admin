# SnowPro Core Practice Questions (25 Total – Official-Style)

---

## Architecture (20%)

1. **What are the three layers of Snowflake architecture?**  
   A: Storage, Compute, Cloud Services (Correct)  
   B: Database, Schema, Table  
   C: Warehouse, Stage, Pipe  

2. **What is stored in micro-partitions?**  
   A: Columnar data, metadata, min/max values (Correct)  
   B: Full table rows  
   C: Indexes  

3. **Can you scale storage independently of compute?**  
   A: Yes (Correct)  
   B: No  
   C: Only in Enterprise edition  

4. **What happens when a warehouse is suspended?**  
   A: Compute stops, storage persists (Correct)  
   B: Data is deleted  
   C: Billing stops completely  

5. **Which feature enables zero-copy cloning?**  
   A: Metadata pointers (Correct)  
   B: Full data copy  
   C: RMAN backup  

---

## Data Loading & Unloading (25%)

6. **Which command loads data from an internal stage?**  
   A: `COPY INTO table FROM @stage/file.csv` (Correct)  
   B: `PUT file @stage`  
   C: `LOAD DATA FROM S3`  

7. **What does `AUTO_INGEST=TRUE` do in a pipe?**  
   A: Enables S3 event notifications (Correct)  
   B: Runs every hour  
   C: Compresses files  

8. **Which file format supports semi-structured data natively?**  
   A: JSON, Parquet, Avro (Correct)  
   B: CSV only  
   C: TXT  

9. **How do you unload data to S3?**  
   A: `COPY INTO @stage FROM table` (Correct)  
   B: `EXPORT TO S3`  
   C: `GET @stage`  

10. **What is the purpose of `ON_ERROR = CONTINUE`?**  
    A: Skip bad records (Correct)  
    B: Fail entire load  
    C: Retry 3 times  

---

## Security & Access Control (20%)

11. **Which role can create other roles?**  
    A: `SECURITYADMIN` (Correct)  
    B: `USERADMIN`  
    C: `SYSADMIN`  

12. **What does `CURRENT_ROLE()` return in a masking policy?**  
    A: Role of the user running the query (Correct)  
    B: Owner of the table  
    C: `ACCOUNTADMIN`  

13. **How do you restrict rows by region?**  
    A: Row Access Policy (Correct)  
    B: View with WHERE  
    C: Clustering key  

14. **Which view shows login failures?**  
    A: `ACCOUNT_USAGE.LOGIN_HISTORY` (Correct)  
    B: `INFORMATION_SCHEMA.LOGINS`  
    C: `QUERY_HISTORY`  

15. **What is required for cross-account data sharing?**  
    A: Secure Share + Business Critical edition (Correct)  
    B: Only Reader accounts  
    C: Public stage  

---

## Performance & Optimization (20%)

16. **What does a clustering key do?**  
    A: Co-locates data in micro-partitions (Correct)  
    B: Creates an index  
    C: Compresses data  

17. **Where do you view query execution details?**  
    A: Query Profile in Snowsight (Correct)  
    B: `QUERY_HISTORY` only  
    C: `WAREHOUSE_EVENTS`  

18. **What causes query spilling to local storage?**  
    A: Insufficient warehouse memory (Correct)  
    B: Too many joins  
    C: Bad clustering  

19. **When should you use a materialized view?**  
    A: Frequently accessed aggregations (Correct)  
    B: Real-time data  
    C: Large fact tables  

20. **How do you check cache hit ratio?**  
    A: Query Profile → "Bytes scanned from cache" (Correct)  
    B: `WAREHOUSE_METERING_HISTORY`  
    C: `RESULT_SCAN`  

---

## Billing, Cost & Administration (15%)

21. **What unit is Snowflake compute billed in?**  
    A: Credits per second (Correct)  
    B: Hours  
    C: Queries  

22. **How do you cap monthly spend?**  
    A: Resource Monitor with `CREDIT_QUOTA` (Correct)  
    B: `ALTER ACCOUNT SET MAX_CREDIT`  
    C: Email Snowflake support  

23. **What is retained after `DROP TABLE`?**  
    A: Time Travel (1 day default) + Fail-safe (7 days) (Correct)  
    B: Nothing  
    C: Only metadata  

24. **Which command enables database replication?**  
    A: `ALTER DATABASE ENABLE REPLICATION TO ACCOUNTS ...` (Correct)  
    B: `CREATE REPLICA`  
    C: `CLONE DATABASE`  

25. **What is the max Time Travel retention (Enterprise)?**  
    A: 90 days (Correct)  
    B: 7 days  
    C: 1 day  

---

## Answers Summary
| Q# | Answer |
|----|--------|
| 1–5 | A, A, A, A, A |
| 6–10 | A, A, A, A, A |
| 11–15 | A, A, A, A, A |
| 16–20 | A, A, A, A, A |
| 21–25 | A, A, A, A, A |

> **Pro Tip**: Use `cert_prep/study_guide.md` + run every script in your trial account. Aim for **90% on mocks** before booking exam.

---
*Curated by Ravi Boppudi | Nov 2025*
