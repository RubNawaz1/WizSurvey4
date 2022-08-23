from pydantic import BaseModel
from pydantic import EmailStr
from datetime import datetime

# properties required during user creation
class UserCreate(BaseModel):
    userfirstname: str
    userlastname: str
    email: EmailStr
    password: str
    CreateDate = datetime
    UpdateDate = datetime
    LastLoginDate = datetime
    

class ShowUser(BaseModel):
    userfirstname: str
    userlastname: str
    email: EmailStr
    status: bool

    class Config:  # to convert non dict obj to json
        orm_mode = True
