import pytest
import json
import csv
from pathlib import Path
from src.lab05.json_csv import json_to_csv, csv_to_json


def test_json_to_csv_basic(tmp_path):
    src = tmp_path / "test.json"
    dst = tmp_path / "test.csv"
    
    data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]
    src.write_text(json.dumps(data), encoding='utf-8')
    
    json_to_csv(str(src), str(dst))
    
    with open(dst, 'r', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    
    assert len(rows) == 2
    assert rows[0]["name"] == "Alice"


def test_csv_to_json_basic(tmp_path):
    src = tmp_path / "test.csv"
    dst = tmp_path / "test.json"
    
    with open(src, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerow({"name": "Alice", "age": "25"})
    
    csv_to_json(str(src), str(dst))
    
    with open(dst, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    assert len(data) == 1
    assert data[0]["name"] == "Alice"


def test_json_to_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        json_to_csv("nonexistent.json", "output.csv")


def test_json_to_csv_invalid_json(tmp_path):
    src = tmp_path / "invalid.json"
    dst = tmp_path / "output.csv"
    
    src.write_text("{invalid json}", encoding='utf-8')
    
    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))