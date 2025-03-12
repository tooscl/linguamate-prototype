from bot.database.session import AsyncSessionLocal
from bot.database.crud import delete_user, delete_user_messages

async def delete_user_info(user_id: int):
    async with AsyncSessionLocal() as db:
        await delete_user_messages(db, user_id)
        await delete_user(db, user_id)
