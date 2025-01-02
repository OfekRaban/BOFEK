from fastapi import APIRouter, HTTPException
from request_body.job import Job as JobSchema
from request_body.user_preferences import UserPreferencesRequestBody
from services.jobs import JobService

router = APIRouter()

# TODO - get job by pref, need to get the phone ,find the pref, and then only filter jobs.
@router.get("/new", response_model=list[JobSchema])
def get_new_jobs_by_preferences(preferences: UserPreferencesRequestBody, limit: int = 50):
    try:
        jobs = JobService.get_new_jobs_by_preferences(preferences, limit)
        return jobs
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Error fetching jobs: {str(e)}")

@router.get("/", response_model=list[JobSchema])
def get_jobs_by_preferences(preferences: UserPreferencesRequestBody, limit: int = 50):
    try:
        jobs = JobService.get_jobs_by_preferences(preferences, limit)
        return jobs
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Error fetching jobs: {str(e)}")

@router.post("/", response_model=list[JobSchema])
def add_jobs(jobs_data: list[JobSchema]):
    try:
        added_jobs = JobService.add_jobs(jobs_data)
        return added_jobs
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error adding jobs: {str(e)}")

@router.delete("/", response_model=dict)
def delete_all_jobs():
    try:
        message = JobService.delete_all_jobs()
        return {"message": message}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting jobs: {str(e)}")
