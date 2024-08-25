import csv

caminho_do_arquivo: str = "aula_03/rel_custo_importacao_201806.csv"

arquivo_csv: list = []

with open(caminho_do_arquivo, mode="r", encoding="utf-8") as arquivo:
    leitor_csv = csv.DictReader(arquivo, delimiter=";")
    
    for linha in leitor_csv:
        arquivo_csv.append(linha)
    
print(f"Qtd de linhas: {len(arquivo_csv)}")
print(arquivo_csv[1])
