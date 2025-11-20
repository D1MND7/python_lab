import json
import csv


def json_to_csv(src_path: str, dst_path: str):
    try:
        with open(src_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        raise ValueError(f"Invalid JSON file: {e}") from e

    if not data:
        with open(dst_path, "w", newline="", encoding="utf-8") as f:
            pass
        return

    fieldnames = data[0].keys()

    with open(dst_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def csv_to_json(src_path: str, dst_path: str):
    try:
        with open(src_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = list(reader)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"CSV file not found: {e}") from e

    with open(dst_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
