from typing import List, Union, Annotated

from jinja2.ext import debug
from loguru import  logger

from faker.proxy import Faker
from fastapi import FastAPI, status, UploadFile, File
from pydantic import BaseModel, EmailStr


class Person(BaseModel):
    first_name: str
    last_name: str
    address: str | None = None
    city: str | None = None
    country: str | None = None
    latlng: dict[float, float] | None = None
    avatar: str | None = None
    birthday: str

class User(BaseModel):
    email: EmailStr
    key: str | None = None


app = FastAPI(debug=True)
faker = Faker()

@app.get("/")
async def hello_world():
    return 'Hello World'


@app.post("/users", status_code=status.HTTP_202_ACCEPTED)
async def get_users(user: User):
    logger.debug(user)
    return user

@app.get("/users/{qty_users}")
async def get_users(qty_users: int = 1):
    return await users_generate(qty_users)

@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}

@app.post("/uploadfile")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

async def users_generate(qty_users):
    users = []
    for _ in range(qty_users):
        user = {
            "first_name": faker.first_name(),
            "last_name": faker.last_name(),
            "address": faker.address(),
            "city": faker.city(),
            "country": faker.country(),
            "latlng": faker.latlng(),
            "avatar": faker.image_url(),
            "birthday": faker.date_of_birth()
        }

        users.append(user)
    return users

