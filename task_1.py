import asyncio
import aiofiles

async def read_file(file_path):
    try:
        async with aiofiles.open(file_path, mode='r', encoding='utf-8') as f:
            content = await f.read()
        return content
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return None
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        return None

async def main():
    file_path = "example.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("Какое-то содержимое файла, бла бла бла.\n")

    content = await read_file(file_path)
    if content:
        print(f"Содержимое файла:\n{content}")

if __name__ == "__main__":
    asyncio.run(main())