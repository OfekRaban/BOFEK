from fastapi import FastAPI
from routers.users import router as users_router
# from routers.jobs import router as jobs_router

app = FastAPI()

app.include_router(users_router, prefix="/users", tags=["Users"])
# app.include_router(jobs_router, prefix="/jobs", tags=["Jobs"])