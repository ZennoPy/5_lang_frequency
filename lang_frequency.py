import re
import sys
from langdetect import detect
from collections import Counter


def load_data(filepath):
    return open(filepath).read()


def pre_treatment_text(text):

    list_of_words = re.findall(r'\w+', text.lower())
    language_text = detect(text)

    if language_text == 'ru':
        stop_words = ['что', 'это', 'так', 'вот', 'быть', 'как', 'в', '—', 'к', 'на', 'для', 'и', 'не', 'с']
        list_of_words_without_stopwords = [word for word in list_of_words if (word not in stop_words)]
    elif language_text == 'en':
        stop_words = ['and', 'to', 'the', 'that', 'in', 'of', 'i', '—', 'with', 'they', 'hem']
        list_of_words_without_stopwords = [word for word in list_of_words if (word not in stop_words)]

    return list_of_words_without_stopwords


def get_most_frequent_words(list_of_words):
    number_of_words = 10
    return Counter(list_of_words).most_common(number_of_words)


if __name__ == '__main__':
    try:
        location_file = sys.argv[1]
        list_get = get_most_frequent_words(pre_treatment_text(load_data(location_file)))
        print("\nThe 10 most popular words in the specified file:\n")
        for index in range(len(list_get)):
            print(list_get[index])
        print("\nThe script completed successfully!")
    except IndexError:
        print("Do not specify the path to the file")
    except FileNotFoundError:
        print("The specified file was not found")
