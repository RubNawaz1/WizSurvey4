from fastapi import APIRouter
from apis.version1.route_create_survey import create_survey
from webapps.auth import route_login
from webapps.users import route_users
from webapps.survey import route_create_survey
from webapps.my_surveys import route_my_survey
from webapps.dashboard import route_dashboard
from webapps.startfromscratch import route_start_from_scratch
from webapps.create_survey import rout_create_survey_dashboard

api_router = APIRouter()
api_router.include_router(route_users.router, prefix="", tags=["users-webapp"])
api_router.include_router(route_login.router, prefix="", tags=["auth-webapp"])
api_router.include_router(route_create_survey.router, prefix="", tags=["survey-webapp"])
api_router.include_router(route_my_survey.router, prefix="", tags=["my_surveys-webapp"])
api_router.include_router(route_dashboard.router, prefix="", tags=["dashboard-webapp"])
api_router.include_router(route_start_from_scratch.router, prefix="", tags=["startfromscratch-webapp"])
api_router.include_router(rout_create_survey_dashboard.router, prefix="", tags=["create_survey-webapp"])