from sqlalchemy.orm import Session 
from typing import   List , Optional
from fastapi import Depends,HTTPException , status , Response , APIRouter 
from .. import schemas , model , oauth2 , utils
from ..database import get_db
from sqlalchemy import func

router = APIRouter(
    prefix="/users",
    tags = ['User Section']
)

@router.post('/create', status_code=status.HTTP_201_CREATED ,response_model = schemas.UserOut)
def createUsers(user_in : schemas.CreateUser , db : Session = Depends(get_db) , user_email : str  = Depends(oauth2.get_current_user)):
    userr = db.query(model.Admin_user).filter(model.Admin_user.email == user_email).first()

    user_in.password = utils.get_password_hash(user_in.password)
    if not userr:
        raise HTTPException(status_code = status.HTTP_203_NON_AUTHORITATIVE_INFORMATION , detail = "you are not allowed to create a user !")
    
    try:
        cache  = model.User(**dict(user_in))
        db.add(cache)
        db.commit()
        db.refresh(cache)
        return cache
    except:
        raise HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED , detail = "the user already exist !")
    

    


