import csv
from pathlib import Path

# Points to the directory where this script lives
BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "sample-simple.csv"

def read_csv_as_rows(file_path):
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        headers = next(reader)
        print(f"Headers: {headers}\n")
        for row in reader:
            print(row)

read_csv_as_rows(CSV_PATH)