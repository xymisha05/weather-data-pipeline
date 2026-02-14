# System Architecture - Automated Weather Data Pipeline 

This diagram shows how data flows through the pipeline from ingestion to storage adn automation.

--------

## Data Flow
Weather API -- extract Script (Python + Requests) -- Transform Script (Pandas Cleaning & Structuring) -- Load Script (SQLAlchemy → PostgreSQL) -- Cron Scheduler (Daily Automation)


---

## 🧠 Explanation

- **Weather API** → Source of hourly weather data  
- **Extract Script** → Fetches raw JSON data  
- **Transform Script** → Cleans and converts data into tabular format  
- **Load Script** → Inserts processed data into PostgreSQL database  
- **Cron Scheduler** → Automates pipeline execution daily  

---

## 🎯 Purpose

Demonstrates a production-style ETL pipeline with automation and database integration, following real-world data engineering workflows.