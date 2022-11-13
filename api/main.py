from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    # Here we'd communicate with the database
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    # Here we'd communicate with the database
    return {"item_id": item_id, "q": q}

@app.get("/technologies")
def read_technologies():
    return {"technologies": ["Python", "FastAPI", "Hadoop", "PostgreSQL", "Docker", "Kubernetes", "Spring Boot", "React", "AWS", "GCP", "Azure"]}