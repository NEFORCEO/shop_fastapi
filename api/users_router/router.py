from fastapi import APIRouter, Response
from sqlalchemy import select

from database.database.func_db import SessionDep
from database.models.users import User
from schemas.user_schemas.schemas import AddUser, LoginUser, ResponseUser

user_router = APIRouter(tags=['Пользователи'],prefix='/me')

@user_router.get('/users')
async def get_users(db: SessionDep):
    res = await db.execute(select(User))
    return res.scalars().all()

@user_router.post("/register", response_model=ResponseUser)
async def get_users(param: AddUser, db:SessionDep):
    all_users = await db.execute(select(User).filter(User.email == param.email))
    ext = all_users.scalar_one_or_none()
    if ext:
        return Response(status_code=409, content="Данный email уже зарегистрован")
    
    new_password  = bin(param.password)[2:]
    new_user = User(
        full_name = param.full_name,
        email = param.email,
        password = new_password
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return {
        "id": new_user.id,
        "full_name": new_user.full_name,
        "email": new_user.email,
        "password": param.password
    } 
    
@user_router.post("/login", response_model=ResponseUser)
async def login(param: LoginUser, db: SessionDep):
    email = await db.execute(select(User).filter(User.email == param.email))
    ext = email.scalar_one_or_none()
    
    if ext:
        if int(bin(param.password)[2:]) == ext.password:
            return {
                "id": ext.id,
                "full_name": ext.full_name,
                "email": ext.email,
                "password": param.password
            }
        else:
            return Response(status_code=404,content="Что то неверно в данных"
            )
    else:
        return Response(status_code=404,content="Придумаю позже"
        )