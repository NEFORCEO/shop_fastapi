from database.database.db import Base
from sqlalchemy import String, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column
from client.config.config import DbConfig

class Product(Base):
    
    __tablename__ = DbConfig.product_name
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, index=True)
    price: Mapped[float] = mapped_column(Float, index=True)
    stock: Mapped[int] = mapped_column(Integer, index=True)
    image_url: Mapped[str] = mapped_column(String, index=True)