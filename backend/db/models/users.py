from db.base_class import Base
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String,DateTime
import datetime

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    userfirstname = Column(String,nullable=False)
    userlastname = Column(String,nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    CreateDate = Column(DateTime,default=datetime.datetime.utcnow)
    UpdateDate = Column(DateTime,default=datetime.datetime.utcnow)
    LastLoginDate = Column(DateTime,default=datetime.datetime.utcnow)
    status = Column(Boolean(), default=True)