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


def frequency_homonymous_word_forms(text):
    # абсолютная и относительная (С УЧЕТОМ/без учета неизменяемых слов) частота омонимичных словоформ
    morph = pymorphy2.MorphAnalyzer()
    result = 0
    clear_text = set(re.findall("[а-яА-Я]+", text))
    for j in clear_text:
        m = morph.parse(j)
        set_of_normal_forms = set([m[i].normal_form for i in range(0, len(m))])
        # print(set_of_normal_forms)
        if len(m) > 1 and len(set_of_normal_forms) == 1:
            result += 1
    return result


def frequency_of_word_forms_with_lexicalmorphological_homonymy(text):
    #абсолютная и относительнаю частота словоформ с лексико-морфологической омонимией
    pass


def maximum_and_average_number_of_homonyms_in_the_text_word_forms(text):
    #максимальное и среднее число омонимов у словоформ текста
    pass


def wordform_with_the_largest_number_of_homonyms(text):
    #словоформы с наибольшим числом омонимов
    pass


def most_frequency_homonym(text):
    #наиболее частотный омоним
    pass


print(usage_count(scientific_text))
print(count_different_word_forms(scientific_text))
print(number_of_unique_lemmas(scientific_text))
print(lexical_richness_of_the_text_index(scientific_text))
print(number_of_unknown_words(scientific_text))
print(frequency_homonymous_word_forms(scientific_text))
