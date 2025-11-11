from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker,DeclarativeBase


from client.config.config import DbConfig


engine = create_async_engine(url=DbConfig.db_name)

magazine_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass