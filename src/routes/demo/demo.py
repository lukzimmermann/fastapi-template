from fastapi import APIRouter
from routes.demo import demoService

router = APIRouter(prefix="/demo", tags=["Demo"])

@router.get("/")
async def root():
    return demoService.say_hello()