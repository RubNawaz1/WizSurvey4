from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/dashboard/")
def dashboard(request: Request):
    return templates.TemplateResponse("general_pages/dashboard.html", {"request": request})
