from sqlalchemy.orm import Session
from typing import   List
from fastapi import Depends,HTTPException , status , APIRouter
from .. import schemas , model , oauth2
from .. import utils
from ..database import get_db
from sqlalchemy import func


router = APIRouter(
    prefix="/token",
    tags = ['Get Your Food Token :)']
)

@router.get('/' , status_code = status.HTTP_201_CREATED)
def get_token(get_token : schemas.getToken , db : Session = Depends(get_db) , user_email : str  = Depends(oauth2.get_current_user)):
    todays_date = db.query(func.current_date()).scalar()
    # todays_date = '2024-05-12'
    cancel_data_overRule = db.query(model.cancelDates).filter(model.cancelDates.user_email == user_email ,
                                               todays_date>= model.cancelDates.start_date,
                                               todays_date<= model.cancelDates.end_date).first()
    if cancel_data_overRule:

        db.delete(cancel_data_overRule)
        db.commit()
        
        
        # user = User.query.get(id)
        # db.session.delete(user)
        # db.session.commit()

        return ('''
                Your Cancellation has been revoked !
                QR(Token) Successfully generated
                ''')
    
    return ('''
                QR(Token)Successfully generated
            ''')
    
    
    
