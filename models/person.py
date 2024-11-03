from pydantic import BaseModel 


class Person(BaseModel):
    id: int
    surname: str
    given_name: str 
    email: str = None 