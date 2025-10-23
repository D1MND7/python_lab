import sys
from lib.text import normalize, tokenize, count_freq, top_n

line = "Привет, мир! Привет!!!" # sys.stdin.readline()

text = tokenize(normalize(line))

max_len = len(sorted(text)[-1])

def info(Beautiful=False):
    if Beautiful:
        print(f'слово{' ' * (max_len - 5)} | частота')
        print(f'{'-' * (max_len + 10)}')

        for _ in top_n(count_freq(text)):
            print(f'{_[0]}{' ' * (max_len - len(_[0]))} | {_[1]}')
        return
    else:
        print(f'Всего слов: {len(text)}')
        print(f'Уникальных слов: {len(set(text))}')
        print(f'Топ-5:')
        for _ in top_n(count_freq(text)):
            print(f'{_[0]}:{_[1]}')

print(info())