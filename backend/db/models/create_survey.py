from db.base_class import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String


class Survey(Base):
    id = Column(Integer, primary_key=True, index=True)
    survey_name = Column(String,nullable=False)
    survey_type = Column(String,nullable=False)
   