import asyncio
import random


async def greet(name):
    await asyncio.sleep(2)
    greeting = random.choice(["мой ненаглядный", "мой ненжый", "дражайший", "лучшая девочка на планете земля по имени"])
    print(f"Привет, {greeting} {name}!")

async def main():
    names = ["Алексей", "Дмитрий", "Михаил", "Александр", "Никита", "Даниил"]  # Список имен
    tasks = [greet(name) for name in names] # создаем корутины
    await asyncio.gather(*tasks) # запуск корутин

asyncio.run(main())