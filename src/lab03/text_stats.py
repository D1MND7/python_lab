import sys
import os

sys.path.append("/Users\dimas\OneDrive\Рабочий стол\python_lab-1\src\lib")
from text import *

text = input()
tokens = []


def main():
    if not text:
        print("Ввод не предоставлен")
        return
    normalized_text = normalize(text)


for word in normalize(text).split():
    clean_word = word.strip('.,!!!!?;:"()[]{}')
    if clean_word:
        tokens.append(clean_word)

total_words = len(tokens)
freq_dict = count_freq(tokens)
unique_words = len(freq_dict)
top_words = top_n(freq_dict, 5)
print(f"Всего слов: {total_words}")
print(f"Уникальных слов: {unique_words}")
print("Топ-5:")
for word, count in top_words:
    print(f"{word}:{count}")

main()
