from sqlalchemy import TIMESTAMP, Column ,Date ,  Integer , Boolean , String, text , ForeignKey
from sqlalchemy.orm import relationship
# from pydantic import EmailStr
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer , primary_key=True , nullable = False)
    password = Column(String , nullable = False)
    email = Column(String , unique= True ,nullable = False )
    created_at = Column(TIMESTAMP(timezone=True) , nullable= False , server_default= text('now()'))

class Admin_user(Base):
    __tablename__ = "adminUsers"

    id = Column(Integer , primary_key = True , nullable = False)
    password = Column(String , nullable = False)
    email = Column(String , unique = True , nullable = False)
    created_at = Column(TIMESTAMP(timezone=True) , nullable = False , server_default=text('now()'))

class cancelDates(Base):
    __tablename__ = "cancellation"

    id = Column(Integer , primary_key= True  ,  nullable = False)
    user_email = Column(String , nullable = False)
    start_date = Column(Date , nullable = False)
    end_date = Column(Date , nullable = False)

class deletionData(Base):
    __tablename__ = "due_data"

    user_email = Column(String , primary_key= True , nullable = False)
    Cancel_month = Column(Integer ,primary_key= True ,  nullable = False)
    cancel_days = Column(Integer , nullable = False)
    paid = Column(Boolean , nullable = False)



    

