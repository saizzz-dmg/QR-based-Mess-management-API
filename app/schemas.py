from pydantic import BaseModel , EmailStr, conint
from datetime import datetime , date
from typing import Optional

class CreateUser(BaseModel):
    email : EmailStr
    password : str

class UserOut(BaseModel):
    id : int
    email:str
    created_at : datetime

class Token(BaseModel):
    access_token : str
    token_type : str

class Tokendata(BaseModel):
    email  : Optional[str]

class cancelDateInput(BaseModel):
    start_date : date
    end_date : date

class getToken(BaseModel):
    entry_date : Optional[date] = None
    
class Due_Input_Format(BaseModel):
    From_date : Optional[date] = None
    Till_date : Optional[date] = None

class Due_Output_Format(BaseModel):
    month : int
    Amount : int






