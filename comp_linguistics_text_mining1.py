from pymystem3 import Mystem
import re
from texts import *
import pymorphy2


def usage_count(text):
    # общее количество словоупотреблений
    result = len(re.findall("[а-яА-Я]+", text))
    return result


def count_different_word_forms(text):
    # число различных словоформ
    clear_text = re.findall("[а-яА-Я]+", text)
    result = len(set(clear_text))
    return result


def number_of_unique_lemmas(text):
    # количество уникальных лемм
    m = Mystem()
    lemmas = m.lemmatize(text)
    lemmatized_text = ''.join(lemmas)
    clear_text = re.findall("[а-яА-Я]+", lemmatized_text)
    result = len(set(clear_text))
    return result


def number_of_unknown_words(text):
    # число незнакомых слов
    morph = pymorphy2.MorphAnalyzer()
    clear_text = set(re.findall("[а-яА-Я]+", text))
    result = sum([not morph.word_is_known(x) for x in clear_text])
    return result


def lexical_richness_of_the_text_index(text):
    # коэффициент лексического богатства текста
    return number_of_unique_lemmas(text)/usage_count(text)


print(usage_count(scientific_text))
print(count_different_word_forms(scientific_text))
print(number_of_unique_lemmas(scientific_text))
print(lexical_richness_of_the_text_index(scientific_text))
print(number_of_unknown_words(scientific_text))
