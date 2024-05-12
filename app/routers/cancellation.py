from sqlalchemy.orm import Session 
from typing import   List , Optional
from fastapi import Depends,HTTPException , status , Response , APIRouter 
from .. import schemas , model , oauth2
import datetime
# from ..utils import verify_password , get_password_hash
from ..database import get_db
from sqlalchemy import func

router = APIRouter(
    prefix="/cancel",
    tags = ['Cancel Mess']
)


@router.post('/', status_code= status.HTTP_201_CREATED)
def cancel(cancel_data : schemas.cancelDateInput , db : Session = Depends(get_db) , email : str  = Depends(oauth2.get_current_user)):
    userr = db.query(model.User).filter(model.User.email == email).first()
    if not userr:
        raise HTTPException(status_code= status.HTTP_203_NON_AUTHORITATIVE_INFORMATION , detail= " Not Authenticated :/")
    mdate1 = datetime.datetime.strptime(f'{cancel_data.start_date}', "%Y-%m-%d").date()
    rdate1 = datetime.datetime.strptime(f'{cancel_data.end_date}', "%Y-%m-%d").date()
    delta =  (rdate1 - mdate1).days
    if delta<3 or delta>7 or cancel_data.start_date<= db.query(func.current_date()).scalar():
        raise HTTPException(status_code = status.HTTP_406_NOT_ACCEPTABLE , detail = "Cancellation dates not acceptable :/")
    cancel_data = dict(cancel_data)
    cancel_data.update({"user_email" : email})
    cache  = model.cancelDates(**cancel_data)
    db.add(cache)
    db.commit()
    db.refresh(cache)
    return cache




@router.post('/pushdue' , status_code = status.HTTP_201_CREATED)
def pushDueDates(cancel_dates : schemas.Due_Input_Format , db: Session = Depends(get_db) , email : str = Depends(oauth2.get_current_user)):
    Admin_user = db.query(model.Admin_user).filter(model.Admin_user.email == email).first()
    if not Admin_user:
        raise HTTPException(status_code = status.HTTP_203_NON_AUTHORITATIVE_INFORMATION , detail = "login as admin user to push out dues :/")
    
    results = db.query(model.cancelDates.user_email,func.sum(model.cancelDates.end_date - model.cancelDates.start_date + 1).label('days')).group_by(model.cancelDates.user_email).filter(
        model.cancelDates.start_date>=cancel_dates.From_date , model.cancelDates.end_date<=cancel_dates.Till_date
    ).all()
    for i,j in results:
        temp_dict = {
            "user_email" : i,
            "cancel_days" : j,
            "Cancel_month" : str(cancel_dates.From_date)[5:7],
            "paid" : False
        }
        try:
            cache =model.deletionData(**dict(temp_dict))
            db.add(cache)
            db.commit()
        except:
            raise HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED , detail = "the dues for the mentioned month have already been pushed !")
    return "successfully updated DUE table !"






@router.get('/kydue' , status_code= status.HTTP_201_CREATED , response_model= List[schemas.Due_Output_Format])
def get_my_due(db : Session = Depends(get_db) , email : str = Depends(oauth2.get_current_user)):
    userr = db.query(model.User).filter(model.User.email == email).first()
    if not userr:
        raise HTTPException(status_code = status.HTTP_203_NON_AUTHORITATIVE_INFORMATION , detail = "You are not authorized :/")
    
    data = db.query(model.deletionData.Cancel_month.label('month') , ((30-(model.deletionData.cancel_days))*107).label("Amount")).filter(model.deletionData.user_email == email).all()

    return data














    
    