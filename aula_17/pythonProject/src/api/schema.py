from pydantic import BaseModel

class PokemonSchema(BaseModel):
    name: str
    types: str
    image: str
    height: int
    weight: int
    number: int

    class Config:
        orm_mode = True