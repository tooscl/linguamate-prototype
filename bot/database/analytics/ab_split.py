from sqlalchemy.ext.asyncio import AsyncSession
import random
from bot.database.models import ABTestUser

async def assign_user_to_ab_test(db: AsyncSession, user_id: int, test_id: int):
    group_name = random.choice(['A', 'B'])
    ab_user = ABTestUser(user_id=user_id, test_id=test_id, group_name=group_name)
    db.add(ab_user)
    await db.commit()
    return ab_user