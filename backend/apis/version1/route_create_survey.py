from schemas.create_survey import ShowSurvey
from db.repository.survey import create_new_survey
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from schemas.create_survey import CreateSurvey
from sqlalchemy.orm import Session

router = APIRouter()
@router.post("/surveyname/", response_model=ShowSurvey)
def create_survey(survey: CreateSurvey, db: Session = Depends(get_db)):
    survey = create_new_survey(survey=survey, db=db)
    return survey
