from typing import Dict, Any

livro: Dict[str, Any] = {
    "titulo":"Como Fazer Amigos e Influenciar pessoas",
    "Auto":"Dale Carnege",
    "Ano":"1960"
}

lista_de_elementos: list = livro.items()

for elemento in lista_de_elementos:
    print(elemento)