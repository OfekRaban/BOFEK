from request_body.job import Job
from repositories.jobs import JobRepository
from sqlalchemy.orm import Session
from typing import List

class JobService:
    def __init__(self, db: Session):
        self.job_repo = JobRepository(db)

    def get_new_jobs_by_preferences(self, preferences: dict, limit: int = 50) -> List[Job]:
        jobs = self.job_repo.get_new_jobs_by_preferences(preferences, limit)
        return jobs

    def get_jobs_by_preferences(self, preferences: dict, limit: int = 50) -> List[Job]:
        jobs = self.job_repo.get_jobs_by_preferences(preferences, limit)
        return jobs

    def add_jobs(self, jobs_data: List[Job]) -> List[Job]:
        try:
            jobs_dicts = [job.model_dump() for job in jobs_data]
            new_jobs = self.job_repo.add_jobs(jobs_dicts)
            return new_jobs
        except Exception as e:
            raise ValueError(f"An error occurred while adding jobs: {str(e)}")

    def delete_all_jobs(self) -> str:
        try:
            rows_deleted = self.job_repo.delete_all_jobs()
            return f"Successfully deleted {rows_deleted} jobs."
        except Exception as e:
            raise ValueError(f"Failed to delete all jobs: {str(e)}")
