import asyncio

LOG_FILE = "chat_log.txt"

async def save_message(msg: str):
    async with asyncio.Lock():
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(msg + "\n")

async def load_recent_messages(n=30, offset=0):
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
            start = max(0, len(lines) - offset - n)
            end = len(lines) - offset
            return lines[start:end]
    except FileNotFoundError:
        return []