import pandas as pd
import json
import glob

def get_latest_file():
    files = glob.glob("data/raw/*.json")
    return max(files)

def transform_data(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)

    hourly = data["hourly"]
    df = pd.DataFrame(hourly)

    return df

def save_processed_data(df):
    output_path = "data/processed/weather_cleaned.csv"
    df.to_csv(output_path, index=False)
    print(f"Saved cleaned data to {output_path}")

def main():
    latest_file = get_latest_file()
    df = transform_data(latest_file)
    save_processed_data(df)

if __name__ == "__main__":
    main()