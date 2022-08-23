from typing import List
from typing import Optional

from fastapi import Request


class surveyCreateForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.surveyname: Optional[str] = None
        self.survey_category: Optional[str] = None
        self.firstCheckbox: Optional[str] = None
        self.password: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.surveyname = form.get("surveyname")
        self.survey_category = form.get("survey_category")
        self.firstCheckbox = form.get("firstCheckbox")
        self.firstRadio = form.get("firstRadio")
        self.secondRadio = form.get("secondRadio")

  