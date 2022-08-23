from db.models.create_survey import Survey
from schemas.create_survey import CreateSurvey
from sqlalchemy.orm import Session

def home(db: Session):
    home = db.query(Survey).all()
    return home

def create_new_survey(survey: CreateSurvey, db: Session):
    survey = Survey(
        survey_name=survey.survey_name, survey_type=survey.survey_type
        
    )
    db.add(survey)
    db.commit()
    db.refresh(survey)
    return survey


def get_survey_by_id(id: int, db: Session):
    survey = db.query(Survey).filter(Survey.id == id).first()
    return survey
