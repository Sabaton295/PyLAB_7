import asyncio
import aiohttp

async def fetch(session, url):
    try:
        async with session.get(url, timeout=10) as response:
            if response.status == 200:
                return await response.text(), response.status
            else:
                return f"Error: Status code {response.status}", response.status
    except aiohttp.ClientError as e:
        return f"Error: {e}", None
    except asyncio.TimeoutError:
        return f"Error: Timeout", None

async def main():
    urls = [
        "https://miet.ru",
        "https://www.google.com",
        "https://www.youtube.com",
        "https://habr.com",
        "https://invalid_url.com", # Пример неверного URL
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        for url, result in zip(urls, results):
            content, status = result if isinstance(result, tuple) else (result, None)
            print(f"URL: {url}")
            print(f"Status: {status}")
            if status == 200:
                print(f"Content: {content[:300]}...\n")
            else:
                print(f"Content: {content}\n")

if __name__ == "__main__":
    asyncio.run(main())