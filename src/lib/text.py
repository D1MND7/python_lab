def normalize(text: str) -> str:
    if not text:
        return ""
    text = text.lower()
    words = text.split()
    return " ".join(words)


def tokenize(text: str) -> list[str]:
    if not text.strip():
        return []
    import re

    words = re.findall(r"\b\w+\b", text.lower())
    return words


def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq


def top_n(freq: dict[str, int], n: int) -> list[tuple[str, int]]:
    items = list(freq.items())
    items.sort(key=lambda x: (-x[1], x[0]))
    return items[:n]
