from database.database.db import Base
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from client.config.config import DbConfig

class User(Base):
    
    __tablename__ = DbConfig.user_name
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    full_name: Mapped[str] = mapped_column(String, index=True)
    email: Mapped[str] = mapped_column(String, index=True)
    password: Mapped[int] = mapped_column(Integer, index=True)