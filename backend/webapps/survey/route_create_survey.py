from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/create_survey/")
def create_survey(request: Request):
    return templates.TemplateResponse("survey/create_survey.html", {"request": request})
