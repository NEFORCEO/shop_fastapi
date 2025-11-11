from fastapi import APIRouter, Response
from sqlalchemy import select

from database.database.func_db import SessionDep
from database.models.category import Category
from schemas.category_schemas.schemas import (
    GetCategory,
    ResponseCategory,
    InputCategory
    )

category_router = APIRouter(tags=["Категории"], prefix='/category')


@category_router.get('/category')
async def get_category(db: SessionDep):
    category = await db.execute(select(Category))
    return category.scalars().all()

@category_router.get('/caterogy/{id}', response_model=ResponseCategory)
async def get_category_num(id: int,  db: SessionDep):
    category = await db.execute(select(Category).filter(Category.id  == id))
    result = category.scalar_one_or_none()
    if result:
        return {
            "id": result.id,
            "name": result.name,
            "description": result.description
        }
    return Response(status_code=404, content="Такой категории не обнаружено")
    
@category_router.post("/category", response_model=ResponseCategory)
async def post_category(param: InputCategory, db: SessionDep):
    category = await db.execute(select(Category).filter(Category.name == param.name))
    result = category.scalar_one_or_none()
    if result:
        return Response(status_code=409, content="Такая категория уже существует")
    new_category = Category(
        name=param.name,
        description=param.description
    )
    db.add(new_category)
    await db.commit()
    await db.refresh(new_category)
    return {
    "id":new_category.id,
    "name": new_category.name,
    "description": new_category.description
    }
    
@category_router.put('/category', response_model=ResponseCategory)
async def put_category(param_id: GetCategory, param: InputCategory, db: SessionDep):
    category = await db.execute(select(Category).filter(Category.id == param_id.id))
    result = category.scalar_one_or_none()
    if not result:
        return Response(status_code=404, content="Такой категории не существует")
    
    if param.name is not None:
        result.name = param.name
    if param.description is not None:
        result.description = param.description
    await db.commit()
    return {
        "id": result.id,
        "name": result.name,
        "description": result.description
    }
    
    
    
@category_router.delete('/category', response_model=ResponseCategory)
async def delete_category(param: GetCategory, db: SessionDep):
    category = await db.execute(select(Category).filter(Category.id == param.id))
    result = category.scalar_one_or_none()
    if not result:
        return Response(status_code=404, content="Такой категории не существует")
    await db.delete(result)
    await db.commit()
    return {
        "id": result.id,
        "name": result.name,
        "description": result.description
    }
    