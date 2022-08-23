from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)

@router.get("/my_surveys/")
def my_surveys(request: Request):
    return templates.TemplateResponse("my_surveys/my_surveys.html", {"request": request})
