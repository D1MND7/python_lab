import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace('ё', 'е')
        text = text.replace('Ё', 'Е')
    while '  ' in text:
        text = text.replace('  ', ' ')
    return text.strip()

def tokenize(text: str) -> list[str]:
    text = re.findall(r'\b[\w\'-]+\b', text)
    return text

def count_freq(tokens: list[str]) -> dict[str, int]:
    dic = {}
    unique = set(tokens)
    for _ in unique:
        dic[_] = tokens.count(_)
    return dic

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda x: x[1], reverse=True)[:n]
