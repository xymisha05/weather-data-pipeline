#  Automated Weather Data Pipeline

Production-style ETL pipeline that ingests real-time weather data, transforms it into structured format, and loads it into a PostgreSQL database with automated scheduling.

##  Key Highlights
- Built full ETL pipeline (Extract → Transform → Load)
- Integrated real-world API data ingestion
- Automated pipeline with cron scheduling
- Stored structured data in PostgreSQL
- Implemented logging and modular architecture
# Automated Weather Data Pipeline

## Overview

This project is an end-to-end ETL data engineering pipeline that extracts weather forecast data from an API, transforms it into a clean structured format, and loads it into a PostgreSQL database.

The pipeline is fully automated and scheduled using cron.

## Features

* Extracts hourly weather data from Open-Meteo API
* Transforms JSON data into clean tabular format
* Loads data into PostgreSQL database
* Automated pipeline runner
* Scheduled execution with cron
* Logging of pipeline runs

## Tech Stack

## Tech Stack
- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- REST API Integration
- Linux (WSL)
- Cron Scheduling

## Pipeline Architecture

Extract → Transform → Load

## How To Run

Run pipeline manually:

python src/run_pipeline.py

## Database Verification

SELECT COUNT(*) FROM weather_hourly;

## Future Improvements

* Add dashboard visualization
* Deploy to cloud (AWS/GCP)
* Add error monitoring
* Add data quality checks

## Author

Amirat Alao
