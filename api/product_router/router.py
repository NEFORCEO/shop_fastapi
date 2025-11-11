from fastapi import APIRouter, Response
from sqlalchemy import select

from database.database.func_db import SessionDep
from database.models.products import Product
from schemas.product_schemas.schemas import (
    AddProduct, 
    ResponseProduct, 
    PesponseNumProduct, 
    DeleteProduct, 
    PatchProduct
    )

product_router = APIRouter(tags=['Продукция'], prefix="/prod")

@product_router.get('/product')
async def get_product(db: SessionDep):
    product_all = await db.execute(select(Product))
    return product_all.scalars().all()


@product_router.get('/product/{id}', response_model=PesponseNumProduct)
async def get_num_product(id: int, db: SessionDep):
    get_product = await db.execute(select(Product).filter(Product.id == id))
    result = get_product.scalar_one_or_none()
    if result:
        return {
            "id": result.id,
            "name": result.name,
            "price": result.price,
            "stock": result.stock,
            "image_url": result.image_url
        }
    return Response(status_code=404, content="Нет такого товара лол")

@product_router.post('/product', response_model=ResponseProduct)
async def register_product(param: AddProduct, db: SessionDep):
    new_product = Product(
        name = param.name,
        price = param.price,
        stock = param.stock,
        image_url = param.image_url
    )
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    return {
        "message": "товар был успешно добавлен",
        "name": new_product.name,
        "price": new_product.price,
        "stock": new_product.stock
    }
    
@product_router.patch('/product', response_model = PesponseNumProduct)
async def patch_product(param: PatchProduct, db: SessionDep):
    patch_product = await db.execute(select(Product).filter(Product.id == param.id))
    result = patch_product.scalar_one_or_none()
    if not result:
        return Response(status_code=404, content="Такого товара не существует")
    
    if param.name is not None:
        result.name = param.name
    if param.price is not None:
        result.price = param.price
    if param.stock is not None:
        result.stock = param.price
    if param.image_url is not None:
        result.image_url = param.image_url
        
    await db.commit()
    await db.refresh(result)
    return {
        "id": result.id,
        "name": result.name,
        "price": result.price,
        "stock": result.stock,
        "image_url": result.image_url   
    }
    
@product_router.delete('/product/{id}', response_model=DeleteProduct)
async def delete_product(id: int, db: SessionDep):
    product = await db.execute(select(Product).filter(Product.id == id))
    result = product.scalar_one_or_none()
    if result:
        await db.delete(result)
        await db.commit()
        return {
            "message": "Продукт был успешно удален",
            "result": True
        }
        

        