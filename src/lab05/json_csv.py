import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    
    json_path = Path(json_path)
    csv_path = Path(csv_path)
    
   
    if not json_path.exists():
        raise FileNotFoundError(f"JSON файл не найден: {json_path}")
    
    
    try:
        with json_path.open('r', encoding='utf-8') as json_file:
            data = json.load(json_file)
    except json.JSONDecodeError as e:
        raise ValueError(f"Ошибка декодирования JSON: {e}")
    
   
    if not data:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список объектов")
    
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы JSON должны быть словарями")
    
    if len(data) == 0:
        raise ValueError("Пустой список в JSON")
    
    
    all_fields = set()
    for item in data:
        all_fields.update(item.keys())
    fieldnames = sorted(all_fields)
    

    try:
        with csv_path.open('w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            
            for item in data:
                
                row = {field: item.get(field, '') for field in fieldnames}
                writer.writerow(row)
                
    except Exception as e:
        raise ValueError(f"Ошибка записи CSV: {e}")


def csv_to_json(csv_path: str, json_path: str) -> None:
    
    csv_path = Path(csv_path)
    json_path = Path(json_path)
    
   
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")
    
   
    try:
        with csv_path.open('r', encoding='utf-8') as csv_file:
            
            sample = csv_file.read(1024)
            csv_file.seek(0)
            
            sniffer = csv.Sniffer()
            dialect = sniffer.sniff(sample)
            has_header = sniffer.has_header(sample)
            
            if not has_header:
                raise ValueError("CSV файл должен содержать заголовок")
            
            reader = csv.DictReader(csv_file, dialect=dialect)
            rows = list(reader)
            
    except Exception as e:
        raise ValueError(f"Ошибка чтения CSV: {e}")
    
  
    if not rows:
        raise ValueError("Пустой CSV файл")
    

    try:
        with json_path.open('w', encoding='utf-8') as json_file:
            json.dump(rows, json_file, ensure_ascii=False, indent=2)
            
    except Exception as e:
        raise ValueError(f"Ошибка записи JSON: {e}")
        