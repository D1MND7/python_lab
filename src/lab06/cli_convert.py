import argparse
import sys
import os

# Получаем абсолютный путь к корню проекта
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, project_root)

try:
    from src.lab05.lab05_csv_xlsx import csv_to_xlsx
    from src.lab05.lab05_json_csv import json_to_csv, csv_to_json
except ImportError as e:
    print(f"Ошибка импорта: {e}")
    print(
        "Убедитесь, что файлы lab05_csv_xlsx.py и lab05_json_csv.py существуют в src/lab05/"
    )
    sys.exit(1)

parser = argparse.ArgumentParser("CLI‑утилиты лабораторной №6")
subparsers = parser.add_subparsers(dest="command")

json2csv_parser = subparsers.add_parser("json2csv", help="Перевести json в csv")
json2csv_parser.add_argument("--in", required=True, dest="input")
json2csv_parser.add_argument("--out", required=True)

csv2json_parser = subparsers.add_parser("csv2json", help="Перевести csv в json")
csv2json_parser.add_argument("--in", required=True, dest="input")
csv2json_parser.add_argument("--out", required=True)

csv2xlsx_parser = subparsers.add_parser("csv2xlsx", help="Перевести csv в xlsx")
csv2xlsx_parser.add_argument("--in", required=True, dest="input")
csv2xlsx_parser.add_argument("--out", required=True)

args = parser.parse_args()

if args.command == "json2csv":
    json_to_csv(args.input, args.out)

if args.command == "csv2json":
    csv_to_json(args.input, args.out)

if args.command == "csv2xlsx":
    csv_to_xlsx(args.input, args.out)
