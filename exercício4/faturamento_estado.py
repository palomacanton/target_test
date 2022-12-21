
#lista estados e valores
est = ['SP','RJ','MG','ES','OUTROS']
vlr = [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]

cemp = sum(vlr)
porcentagem = []

for i in vlr:
    v = i * 100 / cemp
    template = '{:.2f}'
    saida = template.format(v)
    porcentagem.append(saida)


dicionario = dict(zip(est, porcentagem))

print('Porcentagem de cada estado: ' + str(dicionario))
#procurar sobre o split
