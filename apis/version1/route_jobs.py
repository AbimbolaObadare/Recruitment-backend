from typing import List

from db.models.users import Users
from db.repo.jobs import (
    create_new_job,
    delete_job_by_id,
    list_jobs,
    retreive_jobs,
    retreive_jobs_with_id,
    update_job_by_id,
)
from db.repo.users import get_current_user_from_token
from db.session import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from schemas.jobs import JobCreate, ShowJob
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/create-jobs", status_code=status.HTTP_201_CREATED, response_model=ShowJob)
def create_job(
    job: JobCreate,
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user_from_token),
):
    """Create Jobs router"""
    job = create_new_job(job=job, db=db, owner_id=current_user.id)
    return job


@router.get("/all", status_code=status.HTTP_200_OK, response_model=List[ShowJob])
def list_job(db: Session = Depends(get_db)):
    """Get all post from database that are active"""
    jobs = list_jobs(db)
    return jobs


@router.get("/get/{id}", response_model=ShowJob)
def get_job(id: int, db: Session = Depends(get_db)):
    """Get post by id"""
    job = retreive_jobs_with_id(id=id, db=db)
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Job with id:{id} not found")
    return job


@router.put("/update/{id}")
def update_job(
    id: int,
    job: JobCreate,
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user_from_token),
):
    """Update job by id"""
    jobs = retreive_jobs(id=id, db=db)

    if jobs is None:
        print("checking")
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job with id {id} does not exist",
        )

    print(jobs.owner_id, current_user.id, current_user.is_superuser)
    if jobs.owner_id == current_user.id or current_user.is_superuser:
        update_job_by_id(id=id, job=job, db=db)
        return {"detail": "Sucessfully updated"}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not permitted!!!!")


@router.delete("/delete/{id}")
def delete_job(
    id: int,
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user_from_token),
):
    job = retreive_jobs(id=id, db=db)
    if not job:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job with id {id} does not exist",
        )
    print(job.owner_id, current_user.id, current_user.is_superuser)
    if job.owner_id == current_user.id or current_user.is_superuser:
        delete_job_by_id(id=id, db=db)
        return {"detail": "Successfully deleted."}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not permitted!!!!")
