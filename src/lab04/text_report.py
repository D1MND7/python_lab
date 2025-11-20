import re
import argparse
from pathlib import Path
from io_txt_csv import read_text, write_csv


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    else:
        text
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")
    else:
        text
    text = text.strip()
    text = re.sub(r"[\t\r\x00-\x1f\x7F]", " ", text)
    text = " ".join(text.split())
    return text


def tokenize(text: str) -> list[str]:
    pattern = r"\w+(?:-\w+)*"
    tokens = re.findall(pattern, text)
    return tokens


def count_freq(tokens: list[str]) -> dict[str, int]:
    unique_words = list(set(tokens))
    list_count = [tokens.count(i) for i in unique_words]
    dict_count = {key: word for key, word in list(zip(unique_words, list_count))}
    return dict_count


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    list_dict = list(freq.items())
    top = sorted(list_dict, key=lambda x: x[0])
    top_plus = sorted(top, key=lambda x: x[1], reverse=True)[:n]
    return top_plus


def main():
    parser = argparse.ArgumentParser(description="Анализ текста и создание отчета")
    parser.add_argument(
        "--in",
        dest="input_file",
        default="data/lab04/input.txt",
        help="Входной текстовый файл (по умолчанию: data/lab04/input.txt)",
    )
    parser.add_argument(
        "--out",
        dest="output_file",
        default="data/lab04/report.csv",
        help="Выходной CSV файл (по умолчанию: data/lab04/report.csv)",
    )
    parser.add_argument(
        "--encoding",
        default="utf-8",
        help="Кодировка файла (по умолчанию: utf-8, для Windows: cp1251)",
    )
    args = parser.parse_args()

    try:
        print(f"Чтение файла: {args.input_file}")
        text = read_text(args.input_file, encoding=args.encoding)
        print("Анализ текста...")
        normalized = normalize(text)
        tokens = tokenize(normalized)
        word_counts = count_freq(tokens)
        sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
        print(f"Сохранение отчета: {args.output_file}")
        rows = [(word, count) for word, count in sorted_words]
        header = ("word", "count")
        write_csv(rows, args.output_file, header)
        print("\n--- ОТЧЕТ ---")
        print(f"Всего слов: {len(tokens)}")
        print(f"Уникальных слов: {len(word_counts)}")
        print("Топ-5:")
        freq = count_freq(tokens)
        top_words = top_n(freq, 5)
        for word, count in top_words:
            print(f"{word}:{count}")
        print(f"\nОтчет сохранен в: {args.output_file}")

    except FileNotFoundError:
        return "FileNotFoundError"
    except UnicodeDecodeError:
        return "UnicodeDecodeError"
    except Exception:
        return "Exception"


if __name__ == "__main__":
    main()
