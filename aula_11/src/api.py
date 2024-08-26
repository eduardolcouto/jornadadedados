from faker.proxy import Faker
from fastapi import FastAPI

app = FastAPI()
faker = Faker()

@app.get("/")
async def hello_world():
    return 'Hello World'

@app.get("/users")
async def get_users():
    users = []

    for _ in range(10):
        user = {
            "first_name":faker.first_name(),
            "last_name":faker.last_name(),
            "address":faker.address(),
            "city":faker.city(),
            "country": faker.country(),
            "neighborhood":faker.neighborhood(),
            "latlng":faker.latlng(),
            "avatar":faker.image_url()
        }

        users.append(user)

    return users