import sys
import os
from pathlib import Path

# Добавляем корневую директорию проекта в Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from lab05.lab05_json_csv import json_to_csv, csv_to_json
from lab05.lab05_csv_xlsx import csv_to_xlsx


def main():
    """Основная функция тестирования"""
    print("=== Тестирование Lab05: Конвертации JSON, CSV, XLSX ===\n")
    
    # Создаем директорию для выходных файлов
    out_dir = Path('data/out')
    out_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        # 1. JSON → CSV
        print("1. Конвертация JSON → CSV")
        json_to_csv('data/samples/people.json', 'data/out/people_from_json.csv')
        print("   ✓ Успешно: data/out/people_from_json.csv")
        
        # 2. CSV → JSON
        print("2. Конвертация CSV → JSON")
        csv_to_json('data/samples/people.csv', 'data/out/people_from_csv.json')
        print("   ✓ Успешно: data/out/people_from_csv.json")
        
        # 3. CSV → XLSX 
        print("3. Конвертация CSV → XLSX (people)")
        csv_to_xlsx('data/samples/people.csv', 'data/out/people.xlsx')
        print("   ✓ Успешно: data/out/people.xlsx")
        
        # 4. CSV → XLSX 
        print("4. Конвертация CSV → XLSX (cities)")
        csv_to_xlsx('data/samples/cities.csv', 'data/out/cities.xlsx')
        print("   ✓ Успешно: data/out/cities.xlsx")
        
        # 5. Обратная конвертация для проверки обратимости
        print("5. Проверка обратимости JSON ↔ CSV")
        csv_to_json('data/out/people_from_json.csv', 'data/out/people_roundtrip.json')
        json_to_csv('data/out/people_from_csv.json', 'data/out/people_roundtrip.csv')
        print("   ✓ Успешно: выполнены обратные конвертации")
        
        print("\n=== Все операции завершены успешно! ===")
        print("\nСозданные файлы:")
        for file in out_dir.glob('*'):
            print(f"  - {file}")
            
    except Exception as e:
        print(f"\n Ошибка: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())