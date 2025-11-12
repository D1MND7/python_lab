import  argparse # импортируем библиотеку для обработки аргументов командной строки
from src.lib.text import * # импортируем все функции из нашего модуля обработки текста

def cat(text, n):
    file = open(text, "r").readlines() # открываем файл и читаем все строки в список
    if not n: # если флаг -n не установлен (простой вывод)
        for i in file:
            print(i.replace("\n", ""))
    else:
        file = enumerate(file) # если флаг -n установлен (вывод с нумерацией)
                         # добавляем номера строкам с помощью enumerate
        for i in file:
            print(i[0],i[1].replace("\n", ""))


def stats(txt,n):
    file = open(txt, "r").read() # читаем весь файл как одну строку
    txt = top_n(count_freq(tokenize(normalize(file))),n) # обрабатываем текст: нормализуем - разбиваем на слова - считаем частоты - берем топ-N
    for a in txt:
        print(a[1],a[0])

parser = argparse.ArgumentParser("CLI‑утилиты лабораторной №6")
subparsers = parser.add_subparsers(dest="command")

# подкоманда cat
cat_parser = subparsers.add_parser("cat",help = "Вывести содержимое файла")
cat_parser.add_argument("--input",required = True)
cat_parser.add_argument("-n", action="store_true",help = "Нумировать строки")

# подкоманда stats
stats_parser = subparsers.add_parser("stats",help = "Частоты слез")
stats_parser.add_argument("--input",required = True)
stats_parser.add_argument("--top",type = int, default = 5)

args = parser.parse_args() # разбираем аргументы командной строки

if args.command == "cat":
    cat(args.input,args.n)

if args.command == "stats":
    stats(args.input,args.top)