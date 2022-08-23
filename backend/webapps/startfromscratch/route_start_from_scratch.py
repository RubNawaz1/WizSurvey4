from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/startfromscratch/")
def startfromscratch(request: Request):
    return templates.TemplateResponse("survey/startfromscratch.html", {"request": request})