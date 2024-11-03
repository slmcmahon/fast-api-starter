from fastapi import FastAPI
from routers.people import router as people_router
import logging 

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("fast-api-starter")

app = FastAPI()
app.include_router(people_router)


@app.get("/")
def get_version():
    logger.debug("Root endpoint accessed")
    return {"version": "0.1.1"}
