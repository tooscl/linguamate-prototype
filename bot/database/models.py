from asyncpg.pgproto.pgproto import timedelta
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from bot.database.session import Base

class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "public"}

    telegram_id = Column(Integer, primary_key=True)
    username = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    registered_at = Column(DateTime, default=datetime.utcnow)

    # Связь с таблицей сообщений
    messages = relationship("Message", back_populates="user")

class Message(Base):
    __tablename__ = "messages"
    __table_args__ = {"schema": "public"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("public.users.telegram_id"), nullable=False)  # Указываем правильный PK
    role = Column(String, nullable=False)  # "user" или "assistant"
    text = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    expiration_time = Column(DateTime, default=lambda: datetime.utcnow + timedelta(days=2))  # Время истечения

    # Связь с пользователем
    user = relationship("User", back_populates="messages")
