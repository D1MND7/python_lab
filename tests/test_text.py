import pytest
import sys
import os

# Прямо указываем путь к файлу
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/../src"))

# Импортируем напрямую
import importlib.util

spec = importlib.util.spec_from_file_location("text", "src/lib/text.py")
text_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(text_module)
normalize = text_module.normalize
tokenize = text_module.tokenize
count_freq = text_module.count_freq
top_n = text_module.top_n


def test_normalize():
    assert normalize("ПрИвЕт МИР") == "привет мир"
    assert normalize("  много   пробелов  ") == "много пробелов"
    assert normalize("") == ""


def test_tokenize():
    assert tokenize("привет мир") == ["привет", "мир"]
    assert tokenize("один, два. три!") == ["один", "два", "три"]
    assert tokenize("") == []


def test_count_freq():
    tokens = ["яблоко", "банан", "яблоко"]
    result = count_freq(tokens)
    assert result == {"яблоко": 2, "банан": 1}


def test_top_n():
    freq = {"a": 5, "b": 3, "c": 8, "d": 1}
    result = top_n(freq, 2)
    assert result == [("c", 8), ("a", 5)]


def test_top_n_tie():
    freq = {"z": 3, "a": 3, "b": 3}
    result = top_n(freq, 3)
    assert result == [("a", 3), ("b", 3), ("z", 3)]
