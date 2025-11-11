from pydantic import BaseModel, Field, EmailStr

class ResponseUser(BaseModel):
    id: int 
    full_name: str 
    email: str 
    password: int 

class AddUser(BaseModel):
    full_name: str = Field(..., min_length=3, max_length=15)
    email: str = EmailStr
    password: int  = Field(..., ge=10000)
    
class LoginUser(BaseModel):
    email: str = EmailStr
    password: int 