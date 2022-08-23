from typing import List
from typing import Optional

from fastapi import Request


class UserCreateForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.userfirstname: Optional[str] = None
        self.userlastname: Optional[str] = None
        self.email: Optional[str] = None
        self.password: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.userfirstname = form.get("userfirstname")
        self.userlastname = form.get("userlastname")
        self.email = form.get("email")
        self.password = form.get("password")

    async def is_valid(self):
        if not self.userfirstname or not len(self.userfirstname) > 1:
            self.errors.append("userfirstname should be > 1 chars")
        if not self.userlastname or not len(self.userlastname) > 1:
            self.errors.append("userfirstname should be > 1 chars")    
        if not self.email or not (self.email.__contains__("@")):
            self.errors.append("Email is required")
        if not self.password or not len(self.password) >= 8:
            self.errors.append("Password must be > 8 chars")
        if not self.errors:
            return True
        return False