import requests
from pydantic import BaseModel



def get_pokemon(id:int) -> PokemonSchema:
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    if response.status_code == 200:
        data = response.json()
        data_types = data['types']
        data_name = data['name']
        types_list = []
        for type_info in data_types:
            types_list.append(type_info['type']['name'])

        return PokemonSchema(name=data_name, types=types_list)


if __name__ == '__main__':
    print(get_pokemon(608))
