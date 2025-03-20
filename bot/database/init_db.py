import asyncio
from bot.database.session import init_db
import models

async def main():
    await init_db()
    print("База данных и таблицы успешно созданы!")

if __name__ == "__main__":
    asyncio.run(main())
