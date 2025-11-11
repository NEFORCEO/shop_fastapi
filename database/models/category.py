from database.database.db import Base
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from client.config.config import DbConfig

class Category(Base):
    
    __tablename__ = DbConfig.cart_name
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str]  = mapped_column(String, index=True)
    description: Mapped[str] = mapped_column(String, index=True)