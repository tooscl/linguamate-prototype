from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from bot.database.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    telegram_id = Column(Integer, unique=True, nullable=False)
    username = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    registered_at = Column(DateTime, default=datetime.utcnow)

    # Связь с таблицей сообщений
    messages = relationship("Message", back_populates="user")

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.telegram_id"), nullable=False)
    role = Column(String, nullable=False)  # "user" или "assistant"
    text = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    expiration_time = Column(DateTime)  # Время истечения

    # Связь с пользователем
    user = relationship("User", back_populates="messages")
