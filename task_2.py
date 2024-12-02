import asyncio
import random

async def process_data(data):
    delay = random.uniform(0.5, 3)
    await asyncio.sleep(delay)
    processed_data = data ** 2
    print(f"Обработаны данные: {data}, результат: {processed_data}, задержка: {delay:.2f} секунд")
    return processed_data

async def main():
    data_list = [2, 3, 4, 5, 6]
    tasks = [process_data(data) for data in data_list]
    results = await asyncio.gather(*tasks)
    print(f"Все результаты: {results}")

if __name__ == "__main__":
    asyncio.run(main())