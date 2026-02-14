import pandas as pd
from sqlalchemy import create_engine

DB_NAME = "weather_db"
DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_HOST = "localhost"
DB_PORT = "5432"

def main():
    df = pd.read_csv("data/processed/weather_cleaned.csv")

    engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

    # writes table named weather_hourly (replaces if exists for now)
    df.to_sql("weather_hourly", engine, if_exists="replace", index=False)

    print("Loaded data into PostgreSQL table: weather_hourly")
    print("Row count:", len(df))

if __name__ == "__main__":
    main()