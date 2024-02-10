from fastapi import FastAPI
from pydantic import BaseModel


class person(BaseModel):
    name: str
    occupation: str
    address: str

data =[]

app = FastAPI()


@app.post("/person")
async def add_person(Person: person):
    if Person.name == "" or Person.occupation == "" or Person.address == "" :
        return {"Error_message": "Please fill out all fields!"}
    data.append(Person)
    return {"Message": "Person added successfully.", "data": Person}

@app.get("/person")
def get_person():
    return data