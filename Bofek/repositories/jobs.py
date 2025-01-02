from sqlalchemy.orm import Session
from models_orm.job import JobORM
from datetime import datetime, timedelta
from request_body.job import Job as JobSchema
#from request_body.user_preferences import UserPreferencesRequestBody as UserPreferencesSchema


class JobRepository:
    def __init__(self, db: Session):
        self.db = db

    @staticmethod
    def apply_preferences_filter(self, query, preferences: dict):
        if preferences.get('job_type'):
            query = query.filter(JobORM.title.ilike(f"%{preferences['job_type']}%"))
        if preferences.get('field'):
            query = query.filter(JobORM.description.ilike(f"%{preferences['field']}%"))
        if preferences.get('company'):
            query = query.filter(JobORM.company == preferences['company'])
        if preferences.get('location'):
            query = query.filter(JobORM.location == preferences['location'])
        return query

    def get_new_jobs_by_preferences(self, preferences: dict, limit: int = 50):
        yesterday = datetime.now() - timedelta(days=1)
        query = self.db.query(JobORM)
        query = self.apply_preferences_filter(query, preferences)
        result = query.filter(JobORM.posted_date >= yesterday).limit(limit).all()

        return [JobSchema.model_validate(job) for job in result]

    def get_jobs_by_preferences(self, preferences: dict, limit: int = 50):
        query = self.db.query(JobORM)
        query = self.apply_preferences_filter(query, preferences)
        result = query.limit(limit).all()
        return [JobSchema.model_validate(job) for job in result]

    def add_jobs(self, jobs_data: list):

        try:
            new_jobs = [JobORM(**job) for job in jobs_data]
            self.db.add_all(new_jobs)
            self.db.commit()

            return [JobSchema.model_validate(job) for job in new_jobs]
        except Exception as e:
            self.db.rollback()
            raise e

    def delete_all_jobs(self):
        """
        Delete all jobs from the database.
        :return: A success message.
        """
        try:
            self.db.query(JobORM).delete()
            self.db.commit()
            return {"message": "All jobs deleted successfully."}
        except Exception as e:
            self.db.rollback()
            raise e
