from fastapi import APIRouter, Body, Request
from fastapi.responses import JSONResponse
from models.person import Person 
import logging 

router = APIRouter(prefix="/people", tags=["people"])
logger = logging.getLogger("fast-api-starter")

# Get all people
@router.get("/")
async def get_all_people():
    return []

# Get a person by id
@router.get("/{id}")
async def get_person_by_id(id: int, response_model=Person):
    p = Person(id=id, surname="Public", given_name="John", email="jqp@place.com")
    logger.debug(f"Retrieving person: {p.model_dump()}")
    return p
    
@router.post("/", response_model=Person)
async def add_person(request: Request, person: Person = Body(...)):
    logger.debug(f"Received person: {person.model_dump()}")
    return person

@router.put("/{id}", response_model=Person)
async def update_person(id: int, request: Request, person: Person = Body(...)):
    logger.debug(f"Received person: {person.model_dump()} for id {id}")
    return person

@router.delete("/{id}")
async def delete_person(id: int):
    logger.debug(f"Deleting person for id: {id}.")
    return JSONResponse(content={"message": "updated"}, status_code=204)