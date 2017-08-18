import nltk
import re
import sys
from langdetect import detect
from string import punctuation
from string import whitespace
from nltk.corpus import stopwords
from collections import Counter


def load_data(filepath):
    return open(filepath).read()


def pre_treatment_text(text):

    nltk.download('punkt')
    nltk.download('stopwords')
    
    language_text = detect(text)
    text_without_digits = re.sub(r'[\d]+', r'', text).strip()
    tokenize_text = nltk.word_tokenize(text_without_digits)
    tokenize_text_lower = [value.lower() for value in tokenize_text]
    text_without_punctuation = [value for value in tokenize_text_lower if value not in punctuation]
    text_without_whitespace = [value for value in text_without_punctuation if value not in whitespace]
    text_without_quotes = [value.replace("«", "").replace("»", "") for value in text_without_whitespace]
    clean_text = [value for value in text_without_quotes if value != '']

    if language_text == 'ru':
        stop_words = stopwords.words('russian')
        stop_words.extend(['что', 'это', 'так', 'вот', 'быть', 'как', 'в', '—', 'к', 'на', "для"])
        text_without_stopwords = [value for value in clean_text if (value not in stop_words)]
    elif language_text == 'en':
        text_without_stopwords = [value for value in clean_text if (value not in stopwords.words('english'))]

    return text_without_stopwords


def get_most_frequent_words(text_without_stopwords):
    number_of_words = 10
    return Counter(text_without_stopwords).most_common(number_of_words)

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
