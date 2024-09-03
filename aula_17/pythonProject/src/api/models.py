from db import Base
from sqlalchemy import Column, String, Integer, DateTime, func


class Pokemon(Base):
    __tablename__ = 'pokemons'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    type = Column(String)
    image = Column(String)
    height = Column(Integer)
    weight = Column(Integer)
    number = Column(Integer)
    created_at = Column(DateTime, default=func.now())

    def __init__(self,PokemonSchema):
        self.name = PokemonSchema.name
        self.type = PokemonSchema.types
        self.image = PokemonSchema.image
        self.height = PokemonSchema.height
        self.weight = PokemonSchema.weight
        self.number = PokemonSchema.number


    def __repr__(self):
        return f"Pokemon: {self.nome}"
