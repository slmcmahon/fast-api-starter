from fastapi import FastAPI
from routers.people import router as people_router
import logging 
from config import settings

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("fast-api-starter")

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.DESCRIPTION,
    version=settings.APP_VERSION,
    contact=settings.CONTACT)

app.include_router(people_router)


@app.get("/")
def get_version():
    logger.debug("Root endpoint accessed")
    return {
        "name": settings.APP_NAME,
        "version": settings.APP_VERSION
    }
