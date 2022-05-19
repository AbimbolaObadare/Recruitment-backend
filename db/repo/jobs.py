from sqlalchemy import select, update, delete
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


async def list_jobs():
    # TODO: Update to retun only jobs acive and jobs not expired
    job_list = await database.fetch_all(query=select(Job).where(Job.is_active == True))
    return [dict(result) for result in job_list]


async def retreive_jobs(id: int):
    item = await database.fetch_one(query=select(Job).where(Job.id == id))
    return item


async def retreive_jobs_with_id(id: int):
    item = await database.fetch_one(query=select(Job).where((Job.is_active == True) & (Job.id == id)))
    if item is not None:
        print(item)
        return item
    else:
        return None


async def update_job_by_id(id: int, job: JobCreate):
    existing_job = update(Job).where(Job.id == id).values(**job.dict())
    await database.execute(existing_job)
    return existing_job


async def delete_job_by_id(id: int):
    existing_job = delete(Job).where(Job.id == id)
    return await database.execute(existing_job)
