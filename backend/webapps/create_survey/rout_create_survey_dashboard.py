from db.repository.survey import create_new_survey
from db.repository.survey import CreateSurvey
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request
from fastapi.templating import Jinja2Templates
from schemas.create_survey import CreateSurvey
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from webapps.create_survey.forms import CreateSurveyForms


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)
@router.get("/")
def home(request: Request):
    return templates.TemplateResponse("general_pages/homepage.html", {"request": request})

@router.get("/create_survey/")
def register(request: Request):
    return templates.TemplateResponse("survey/startfromscratch.html", {"request": request})

@router.post("/create_survey/")
async def create_survey(request: Request, db: Session = Depends(get_db)):
    form = CreateSurveyForms(request)
    await form.load_data()
    if await form.is_valid():
        survey = CreateSurvey(
            survey_name=form.survey_name,survey_type=form.survey_type
            )
        try:
            survey = create_new_survey(survey=survey, db=db)
            return templates.TemplateResponse("survey/startfromscratch_dashbord.html", form.__dict__)
           
        except IntegrityError:
            form.__dict__.get("errors").append("Duplicate email")
            return templates.TemplateResponse("users/register.html", form.__dict__)
    return templates.TemplateResponse("users/register.html", form.__dict__)


#  try:
#             user = create_new_user(user=user, db=db)
#             return templates.TemplateResponse("auth/login.html", form.__dict__)
#             # return responses.RedirectResponse(
#             #     "/?msg=Successfully-Registered", status_code=status.HTTP_302_FOUND
#             # )  # default is post request, to use get request added status code 302
#         except IntegrityError:
#             form.__dict__.get("errors").append("Duplicate email")
#             return templates.TemplateResponse("users/register.html", form.__dict__)
#     return templates.TemplateResponse("users/register.html", form.__dict__)