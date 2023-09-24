"""
Вы очень любите считать. Не важно что, где и когда, главное посчитать все, что можно.
Вам на вход приходит текст. Ваша программа должна посчитать количество слов в этом тексте и вывести на печать 10
самых частых слов. Если слова встречаются одинаковое количество раз, то они должны быть отсортированы по алфавиту.

Ограничения:
- игнорируем знаки препинания (тире, запятые, многоточия и т.п.)
- слово, это все то, что отделено пробелом, символом табуляции или символом перевода строки.
- регистр игнорируется
- слова короче 3-х символов игнорируются.


Советы:
1) почитать про регулярные выражения в питоне, для визуального представления можно пользоваться сайтом https://regex101.com/
2) вспомнить про sorted, почитать про lambda функции и сортировку с их помощью

для тестирования запустить pytest 2_task/test.py
"""

import re
from collections import Counter


# def top_10_most_common_words(text: str) -> dict[str, int]:
#     words = re.findall(r'\b\w{3,}\b', text.lower())
#     counted_words = list(Counter(words).items())
#     words_top = sorted(counted_words, key=lambda word: (-word[1], word[0]))
#     return dict(words_top[:10])

def top_10_most_common_words(text: str) -> dict[str, int]:
    words = re.findall(r'\b\w{3,}\b', text.lower())
    return dict(Counter(sorted(words)).most_common(10))
