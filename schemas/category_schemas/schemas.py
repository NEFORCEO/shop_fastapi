

from pydantic import BaseModel


class GetCategory(BaseModel):
    id: int 
    
class ResponseCategory(BaseModel):
    id: int 
    name: str 
    description: str 
    
    
class InputCategory(BaseModel):
    name: str 
    description: str 
    