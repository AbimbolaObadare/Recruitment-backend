<<<<<<< HEAD
from sqlalchemy import select
=======
from sqlalchemy import select, update, delete
>>>>>>> async-sql
from db.models.jobs import Job
from schemas.jobs import JobCreate
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import database


async def create_new_job(job: JobCreate, db: AsyncSession, owner_id: int):
    job_obj = Job(**job.dict(), owner_id=owner_id)
    db.add(job_obj)
    await db.commit()
    await db.refresh(job_obj)
    return job_obj


<<<<<<< HEAD
async def list_jobs(db: AsyncSession):
=======
async def list_jobs():
>>>>>>> async-sql
    # TODO: Update to retun only jobs acive and jobs not expired
    job_list = await database.fetch_all(query=select(Job).where(Job.is_active == True))
    return [dict(result) for result in job_list]


<<<<<<< HEAD
def retreive_jobs(id: int, db: AsyncSession):
    item = db.query(Job).filter(Job.id == id).first()
    return item


async def retreive_jobs_with_id(id: int, db: AsyncSession):
    item = await database.fetch_one(query=select(Job).where(Job.is_active == True).where(Job.id == id))
=======
async def retreive_jobs(id: int):
    item = await database.fetch_one(query=select(Job).where(Job.id == id))
    return item


async def retreive_jobs_with_id(id: int):
    item = await database.fetch_one(query=select(Job).where((Job.is_active == True) & (Job.id == id)))
>>>>>>> async-sql
    if item is not None:
        print(item)
        return item
    else:
        return None

    

<<<<<<< HEAD
def update_job_by_id(id: int, job: JobCreate, db: AsyncSession):
    existing_job = db.query(Job).filter(Job.id == id)
    existing_job.update(job.__dict__)
    db.commit()
    return existing_job.first()


def delete_job_by_id(id: int, db: AsyncSession):
    existing_job = db.query(Job).filter(Job.id == id)
    if not existing_job.first():
        return 0
    existing_job.delete(synchronize_session=False)
    db.commit()
    return 1
=======
async def update_job_by_id(id: int, job: JobCreate):
    existing_job = update(Job).where(Job.id == id).values(**job.dict())
    await database.execute(existing_job)
    return existing_job


async def delete_job_by_id(id: int):
    existing_job = delete(Job).where(Job.id == id)
    return await database.execute(existing_job)
>>>>>>> async-sql
