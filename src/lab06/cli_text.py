import argparse
import sys
import os

# Добавляем путь к корню проекта
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from src.lib.text import *
except ImportError:
    # Если импорт не работает, определяем функции прямо здесь
    import re
    from collections import Counter
    
    def normalize(text):
        return text.lower()
    
    def tokenize(text):
        words = re.findall(r'\b\w+\b', text)
        return words
    
    def count_freq(words):
        return Counter(words)
    
    def top_n(word_counts, n=5):
        return word_counts.most_common(n)

def cat(text, n):
    file = open(text, "r").readlines()
    if not n:
        for i in file:
            print(i.replace("\n", ""))
    else:
        file = enumerate(file)
        for i in file:
            print(i[0], i[1].replace("\n", ""))

def stats(txt, n):
    file = open(txt, "r").read()
    txt = top_n(count_freq(tokenize(normalize(file))), n)
    for a in txt:
        print(a[1], a[0])

parser = argparse.ArgumentParser("CLI‑утилиты лабораторной №6")
subparsers = parser.add_subparsers(dest="command")

cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
cat_parser.add_argument("--input", required=True)
cat_parser.add_argument("-n", action="store_true", help="Нумировать строки")

stats_parser = subparsers.add_parser("stats", help="Частоты слез")
stats_parser.add_argument("--input", required=True)
stats_parser.add_argument("--top", type=int, default=5)

args = parser.parse_args()

if args.command == "cat":
    cat(args.input, args.n)

if args.command == "stats":
    stats(args.input, args.top)