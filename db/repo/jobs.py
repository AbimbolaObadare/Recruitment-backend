from fastapi import APIRouter, Depends, HTTPException, status
from db.models.jobs import Job
from schemas.jobs import JobCreate
from sqlalchemy.orm import Session


def create_new_job(job: JobCreate, db: Session, owner_id: int):
    job_obj = Job(**job.dict(), owner_id=owner_id)
    db.add(job_obj)
    db.commit()
    db.refresh(job_obj)
    return job_obj


def list_jobs(db: Session):
    # TODO: Update to retun only jobs acive and jobs not expired
    jobs = db.query(Job).filter(Job.is_active == True).all()
    return jobs


def retreive_jobs(id: int, db: Session):
    item = db.query(Job).filter(Job.id == id).first()
    return item


def retreive_jobs_with_id(id: int, db: Session):
    item = db.query(Job).filter(Job.id == id).filter(Job.is_active == True)
    return item


def update_job_by_id(id: int, job: JobCreate, db: Session):
    existing_job = db.query(Job).filter(Job.id == id)
    existing_job.update(job.__dict__)
    db.commit()
    return existing_job.first()


def delete_job_by_id(id: int, db: Session):
    existing_job = db.query(Job).filter(Job.id == id)
    if not existing_job.first():
        return 0
    existing_job.delete(synchronize_session=False)
    db.commit()
    return 1
