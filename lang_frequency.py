import os
import sys
from string import punctuation
from collections import Counter


def load_data(filepath):
    if not os.path.isfile(filepath):
        return "The specified file does not exist"
    return open(filepath).read()


def pre_treatment_text(text):
    if not isinstance(text, str):
        raise TypeError('text должен быть str')
    text_without_punctuation = ''.join(x for x in text if x not in punctuation)
    return text_without_punctuation


def get_most_frequent_words(cleaned_text):
    number_of_words = 10
    return Counter(cleaned_text.split(' ')).most_common(number_of_words)

if __name__ == '__main__':
    try:
        location_file = sys.argv[1]
        print("\n10 самых популярных слов в указанном файле:\n")
        list_get = get_most_frequent_words(pre_treatment_text(load_data(location_file)))
        for index in range(len(list_get)):
            print(list_get[index])
        print("\nРабота скрипта успешно завершена!")
    except IndexError:
        print("Не указан путь до файла")
