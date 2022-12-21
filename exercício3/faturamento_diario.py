import json

#formatação para trazer dados json para pyhon
with open("dados.json", encoding='utf-8') as js:
    dados = json.load(js)

#processo para encontrar o máximo e o mínimo
lista_v = []

for i in dados:
    v = i['valor']
    lista_v.append(v)

lista_format = [lista for lista in lista_v if lista > 0.0]
max = max(lista_format)
min = min(lista_format)

#processo para encontrar o faturamento acima da média
fat = []

for i in lista_format:
    tam = len(lista_format)
    med = sum(lista_format)/ tam
    if i > med:
        fat.append(i)
    tam_fat = len(fat)

#resultado output de todos os processos
print("O maior faturamento em um dia do mês: " + str(max))
print("O menor faturamento em um dia do mês: " + str(min))
print("Número de dias com faturamento superior à média mensal: " + str(tam_fat))
