import subprocess
import sys

def run(cmd):
    print(f"\nRunning: {' '.join(cmd)}")
    result = subprocess.run(cmd, check=False)
    if result.returncode != 0:
        print("Command failed.")
        sys.exit(result.returncode)

def main():
    run(["python", "src/extract_weather.py"])
    run(["python", "src/transform_weather.py"])
    run(["python", "src/load_to_postgres.py"])
    print("\n✅ Pipeline complete: Extract → Transform → Load")

if __name__ == "__main__":
    main()