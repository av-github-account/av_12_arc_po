import aiohttp
import asyncio
from collections import Counter

async def get_text(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


@profile
async def main():
    words_file = "words.txt"
    url = "https://eng.mipt.ru/why-mipt/"

    # Асинхронная загрузка текста
    text = await get_text(url)
    word_frequencies = Counter(text.split())

    # Чтение уникальных слов из файла
    with open(words_file, 'r') as file:
        words_to_count = {line.strip() for line in file if line.strip()}

    # Сбор результатов
    frequencies = {word: word_frequencies.get(word, 0) for word in words_to_count}
    
    print(frequencies)

if __name__ == "__main__":
    asyncio.run(main())