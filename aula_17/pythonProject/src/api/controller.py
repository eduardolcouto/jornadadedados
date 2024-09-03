import time
import random
import requests

from db import SessionLocal, engine, Base
from models import Pokemon
from schema import PokemonSchema

Base.metadata.create_all(bind=engine)

def fetch_pokemons_data(pokemon_id):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}')
    if response.status_code == 200:
        data = response.json()

        data_types = data['types']
        data_name = data['name']
        data_image = data['sprites']['other']['official-artwork']['front_default']
        data_number = data['id']
        data_height = data['height']
        data_weight = data['weight']
        types = ', '.join(type['type']['name'] for type in data_types)

        return PokemonSchema(name=data_name, types=types, image=data_image, number=data_number, height=data_height, weight=data_weight)

    else:
        return None

def add_pokemon_to_db(pokemon: PokemonSchema):
    with SessionLocal() as db:
        db_pokemon = Pokemon(pokemon)
        db.add(db_pokemon)
        db.commit()
        db.refresh(db_pokemon)
    return db_pokemon

def get_pokemon_from_db(pokemon_id: int):
    db = SessionLocal()
    pokemon = db.query(Pokemon).filter(Pokemon.id == pokemon_id).first()
    db.close()
    return pokemon


# def main():
#     while True:
#         pokemon_id = random.randint(1,1302)
#         pokemon_schema = fetch_pokemons_data(pokemon_id)
#         if pokemon_schema:
#             add_pokemon_to_db(pokemon_schema)
#             print(f'Pokemon {pokemon_schema.name} adicionado ao banco de dados')
#         else:
#             print(f'Pokemon com id {pokemon_id} não encontrado')
#         time.sleep(10)
def main():
    for i in range(1, 1302):
        pokemon_schema = fetch_pokemons_data(i)
        if pokemon_schema:
            add_pokemon_to_db(pokemon_schema)
            print(f'Pokemon {pokemon_schema.name} adicionado ao banco de dados')
        else:
            print(f'Pokemon com id {i} não encontrado')
        #time.sleep(1)
if __name__ == '__main__':

    main()