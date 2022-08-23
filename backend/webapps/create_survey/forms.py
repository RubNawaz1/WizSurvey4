from typing import List
from typing import Optional
from fastapi import Request

class CreateSurveyForms:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.survey_name: Optional[str] = None
        self.survey_type: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.survey_name = form.get("survey_name")
        self.survey_type = form.get("survey_type")

    async def is_valid(self):
        if not self.survey_name or not len(self.survey_name) > 1:
            self.errors.append("Survey Name should be > 1 chars")
        if not self.survey_type or not len(self.survey_type) > 1:
            self.errors.append("Survey Type should be > 1 chars")    
        if not self.errors:
            return True
        return False