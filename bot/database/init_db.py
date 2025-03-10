import asyncio
from bot.database.session import init_db
from models import User, Message

async def main():
    await init_db()
    print("База данных и таблицы успешно созданы!")

if __name__ == "__main__":
    asyncio.run(main())
