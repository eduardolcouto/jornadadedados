from typing import Dict, Union

GenericSchema = Dict[str, Union[str, float, int]]

UserSchema: GenericSchema = {
    "name": str,
    "city": str,
    "country":str
}