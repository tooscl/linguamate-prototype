from asyncpg.pgproto.pgproto import timedelta
from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey, CheckConstraint, func
from sqlalchemy.orm import relationship
from datetime import datetime
from bot.database.session import Base

class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "public"}

    user_id = Column(Integer, primary_key=True)
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

#  === Таблицы для проведения А/Б-тестов
class ABTest(Base):
    __tablename__ = 'ab_tests'

    id = Column(Integer, primary_key=True)
    test_name = Column(String, nullable=False)
    start_date = Column(DateTime, nullable=False, default=func.now())
    end_date = Column(DateTime, nullable=True)
    metric_name = Column(String, nullable=False)
    description = Column(String)

    users = relationship("ABTestUser", back_populates="test")
    results = relationship("ABTestResult", back_populates="test")


class ABTestUser(Base):
    __tablename__ = 'ab_test_users'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    test_id = Column(Integer, ForeignKey('ab_tests.id'))
    group_name = Column(String, nullable=False)

    __table_args__ = (CheckConstraint("group_name IN ('A', 'B')"),)

    test = relationship("ABTest", back_populates="users")


class ABTestResult(Base):
    __tablename__ = 'ab_test_results'

    id = Column(Integer, primary_key=True)
    test_id = Column(Integer, ForeignKey('ab_tests.id'))
    user_id = Column(Integer, nullable=False)
    metric_value = Column(Numeric, nullable=False)
    timestamp = Column(DateTime, nullable=False, default=func.now())

    test = relationship("ABTest", back_populates="results")