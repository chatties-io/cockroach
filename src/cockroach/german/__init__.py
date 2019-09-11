import aiohttp


CHECK_URL = "https://de.thefreedictionary.com"


async def check_word(session, word: str) -> bool:
    """Check if *word* exists in the German language."""
    target = f"{CHECK_URL}/{word.lower()}"
    async with session.get(target) as response:
        content = await response.text()
        return "Das Wort konnte im Wörterbuch nicht gefunden werden." \
            not in content
