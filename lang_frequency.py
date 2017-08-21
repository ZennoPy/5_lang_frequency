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
    tokenize_text_lower = [value_token.lower() for value_token in tokenize_text]
    tokenize_text_without_punctuation = [value_token for value_token in tokenize_text_lower if value_token
                                         not in punctuation]
    tokenize_text_without_whitespace = [value_token for value_token in tokenize_text_without_punctuation if value_token
                                        not in whitespace]
    tokenize_text_without_quotes = [value_token.replace("«", "").replace("»", "") for value_token
                                    in tokenize_text_without_whitespace]
    tokenize_clean_text = [value_token for value_token in tokenize_text_without_quotes if value_token != '']

    if language_text == 'ru':
        stop_words = stopwords.words('russian')
        stop_words.extend(['что', 'это', 'так', 'вот', 'быть', 'как', 'в', '—', 'к', 'на', "для"])
        tokenize_text_without_stopwords = [value_token for value_token in tokenize_clean_text if
                                           (value_token not in stop_words)]
    elif language_text == 'en':
        tokenize_text_without_stopwords = [value_token for value_token in tokenize_clean_text if
                                           (value_token not in stopwords.words('english'))]

    return tokenize_text_without_stopwords


def get_most_frequent_words(tokenize_text_without_stopwords):
    number_of_words = 10
    return Counter(tokenize_text_without_stopwords).most_common(number_of_words)

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
