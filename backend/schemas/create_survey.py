from pydantic import BaseModel
# properties required during survey creation
class CreateSurvey(BaseModel):
    survey_name: str
    survey_type: str
class ShowSurvey(BaseModel):
    survey_name: str
    survey_type: str
    class Config:  # to convert non dict obj to json
        orm_mode = True
