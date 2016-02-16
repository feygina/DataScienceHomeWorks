from pymystem3 import Mystem
from texts import *
import pymorphy2


def make_clear_text(text):
    # текст без спец символов/цифр/пунктуации
    m = Mystem()
    clear_text = []
    lm = m.analyze(text.lower())
    for i in range(0, len(lm)):
        if 'analysis' in lm[i]:
            clear_text.append(lm[i]['text'])
    return clear_text


def no_one_symbol_text(text):
    # убираем слова состоящие из одного символа
    for i in text:
        if len(i) == 1:
            text.remove(i)
    return text


def usage_count(text):
    # общее количество словоупотреблений
    # result = len(re.findall("[а-яА-Я]+", text))
    result = len(make_clear_text(text))
    print("Общее количество словоупотреблений: ", result)
    return result


def count_different_word_forms(text):
    # число различных словоформ
    clear_text = make_clear_text(text)
    result = len(set(clear_text))
    print("Число различных словоформ: ", result)


def number_of_unique_lemmas(text):
    # количество уникальных лемм
    m = Mystem()
    lemmas = m.lemmatize(text)
    lemmatized_text = ''.join(lemmas)
    clear_text = make_clear_text(lemmatized_text)
    clear_text = no_one_symbol_text(clear_text)
    result = len(set(clear_text))
    print("Количество уникальных лемм: ", result)
    return result


def number_of_unknown_words(text):
    # число незнакомых слов
    morph = pymorphy2.MorphAnalyzer()
    clear_text = set(no_one_symbol_text(make_clear_text(text)))
    result = sum([not morph.word_is_known(x) for x in clear_text])
    print("Число незнакомых слов: ", result)


def lexical_richness_of_the_text_index(text):
    # коэффициент лексического богатства текста
    result = number_of_unique_lemmas(text)/usage_count(text)
    print("Коэффициент лексического богатства текста:", result)


def frequency_homonymous_word_forms(text):
    # абсолютная и относительная (без учета неизменяемых слов) частота омонимичных словоформ
    morph = pymorphy2.MorphAnalyzer()
    result = 0
    clear_text = set(no_one_symbol_text(make_clear_text(text)))
    for j in clear_text:
        # set_of_normal_forms = set([m[i].normal_form for i in range(0, len(m))])
        # print(set_of_normal_forms)
        m = morph.parse(j)
        for k in range(0, len(m)):
            lexeme = []
            unchangeable_tag = []
            unchangeable_tag.append('Fixd' in m[k].tag)
            unchangeable = []
            lex = m[k].lexeme
            for i in lex:
                lexeme.append(i.word)
            lexeme = set(lexeme)
            unchangeable.append(len(lexeme) == 1)
        unchangeable = unchangeable + unchangeable_tag
        if len(m) > 1 and True not in unchangeable:
            result += 1
    print("Абсолютная частота омонимичных словоформ без учета неизменяемых слов: ", result)
    print("Относительная частота омонимичных словоформ без учета неизменяемых слов: ", result/len(clear_text))


def frequency_homonymous_word_forms_full(text):
    # абсолютная и относительная (с учетом неизменяемых слов) частота омонимичных словоформ
    morph = pymorphy2.MorphAnalyzer()
    result = 0
    clear_text = set(no_one_symbol_text(make_clear_text(text)))
    for j in clear_text:
        m = morph.parse(j)
        # set_of_normal_forms = set([m[i].normal_form for i in range(0, len(m))])
        # print(set_of_normal_forms)
        if len(m) > 1:
            result += 1
    print("Абсолютная частота омонимичных словоформ с учетом неизменяемых слов: ", result)
    print("Относительная частота омонимичных словоформ с учетом неизменяемых слов: ", result/len(clear_text))


def frequency_of_word_forms_with_lexicalmorphological_homonymy(text):
    # абсолютная и относительнаю частота словоформ с лексико-морфологической омонимией
    morph = pymorphy2.MorphAnalyzer()
    result = 0
    clear_text = set(no_one_symbol_text(make_clear_text(text)))
    for j in clear_text:
        m = morph.parse(j)
        set_of_lexem = set([m[i][4][0][2] for i in range(0, len(m))])
        # print(set_of_normal_forms)
        if len(m) > 1 and len(set_of_lexem) != 1:
            result += 1
    print("Абсолютная частота словоформ с лексико-морфологической омонимией: ", result)
    print("Относительная частота словоформ с лексико-морфологической омонимией: ", result/len(clear_text))


def maximum_and_average_number_of_homonyms_in_the_text_word_forms(text):
    # максимальное и среднее число омонимов у словоформ текста
    morph = pymorphy2.MorphAnalyzer()
    result = {}
    max_homonym = 0
    mean_homonym = 0
    counter = 0
    clear_text = no_one_symbol_text(make_clear_text(text))
    for j in clear_text:
        set_of_lexem = []
        if j not in result:
            result[j] = 0
        m = morph.parse(j)
        # if morph.word_is_known(j):
            # set_of_lexem = set([m[i][4][0][2] for i in range(0, len(m))])
        # set_of_normal_forms = set([m[i].normal_form for i in range(0, len(m))])
        if len(m) > 1:
            result[j] += 1
            counter += 1
            mean_homonym += len(m)
            if len(m) > max_homonym:
                max_homonym = len(m)
                wordform_with_max_homonym = j
    print("Максимальное число омонимов у словоформ: ", max_homonym)
    print("Среднее число омонимов у словоформ: ", mean_homonym/counter)
    print("Словоформа с наибольшим числом омонимов: ", wordform_with_max_homonym)
    print("Наиболее частотный омоним: ",  max(result, key=result.get))


# def wordform_with_the_largest_number_of_homonyms(text):
#     # словоформы с наибольшим числом омонимов
#     pass
#
#
# def most_frequent_homonym(text):
#     # наиболее частотный омоним
#     homonyms_dictionary = maximum_and_average_number_of_homonyms_in_the_text_word_forms(text)
#     return max(homonyms_dictionary, key=homonyms_dictionary.get)


# usage_count(scientific_text)
count_different_word_forms(scientific_text)
# number_of_unique_lemmas(scientific_text)
lexical_richness_of_the_text_index(scientific_text)
number_of_unknown_words(scientific_text)
frequency_homonymous_word_forms_full(test_text)
frequency_homonymous_word_forms(test_text)
frequency_of_word_forms_with_lexicalmorphological_homonymy(test_text)
maximum_and_average_number_of_homonyms_in_the_text_word_forms(artistic_text)

