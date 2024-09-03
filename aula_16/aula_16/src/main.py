from typing import Optional

from sqlmodel import Field, SQLModel, Session, create_engine

from faker.proxy import Faker

faker = Faker()

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None

engine = create_engine("sqlite:///database.db", echo=False)

SQLModel.metadata.create_all(engine)

hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

with Session(engine) as session:
    for _ in range(1000000):
        session.add(Hero(name=faker.name(), secret_name=faker.last_name(), age=faker.random_int(min=18, max=50)))
    session.commit()