# optimized.py
import requests
from collections import Counter

def get_text(url):
    response = requests.get(url)
    return response.text


@profile
def main():
    words_file = "words.txt"
    url = "https://eng.mipt.ru/why-mipt/"

    # Загрузка текста и подсчёт частот один раз
    text = get_text(url)
    word_frequencies = Counter(text.split())

    # Чтение уникальных слов из файла
    with open(words_file, 'r') as file:
        words_to_count = {line.strip() for line in file if line.strip()}

    # Сбор результатов из предвычисленного словаря
    frequencies = {word: word_frequencies.get(word, 0) for word in words_to_count}
    
    print(frequencies)

if __name__ == "__main__":
    main()