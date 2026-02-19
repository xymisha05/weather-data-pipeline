# Automated Weather Data Pipeline

## Overview
This project is an end-to-end ETL pipeline that collects real-time weather data from a public API, transforms the data into a clean dataset, and loads it into a PostgreSQL database. The pipeline is automated using cron to run daily.

## Architecture
API → Python → Pandas → PostgreSQL → Cron Automation

## Features
- Extracts real-time weather data using REST API
- Cleans and transforms JSON data using pandas
- Loads processed data into PostgreSQL database
- Automated daily pipeline execution using cron
- Logging of pipeline runs

## Tech Stack
- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- Linux (WSL)
- Cron

## How To Run
python src/run_pipeline.py

## Database Verification
SELECT COUNT(*) FROM weather_hourly;

## Future Improvements
- Add dashboard visualization
- Deploy to cloud
- Add error monitoring