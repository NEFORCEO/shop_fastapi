from typing import Annotated

from database.database.db import engine, Base, AsyncSession, magazine_session
from fastapi import Depends


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
async def get_sess() -> AsyncSession:
    async with magazine_session() as session:
        yield session 
        
SessionDep = Annotated[AsyncSession, Depends(get_sess)]
    