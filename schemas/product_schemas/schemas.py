from pydantic import BaseModel



class PesponseNumProduct(BaseModel):
    id: int 
    name: str 
    price: int
    stock: int 
    image_url: str 


class ResponseProduct(BaseModel):
    message: str 
    name: str 
    price: int | float
    stock: int 


class AddProduct(BaseModel):
    name: str 
    price: int | float
    stock: int 
    image_url: str | None = None 
    
class PatchProduct(BaseModel):
    id: int 
    name: str | None = None
    price: int | float| None = None
    stock: int | None = None
    image_url: str | None = None 
    
    
class DeleteProduct(BaseModel):
    message: str 
    result: bool = False
    