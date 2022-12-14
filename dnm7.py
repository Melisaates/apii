from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel, EmailStr

app=FastAPI()
class UserIn(BaseModel):
    username: str
    password:str
    email:EmailStr
    full_name:Union[str,None]=None

class UserOut(BaseModel):
    username:str
    email:EmailStr
    full_name:Union[str,None]=None


@app.post("/user/",response_model=UserOut)
async def creat_user(user:UserIn):
    return user