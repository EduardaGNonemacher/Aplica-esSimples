from itertools import zip_longest, count

Indice = count()
Cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Outro']
Estados = ['SP', 'MG','BA']

CidadeEstado = zip_longest(
    Estados,
    Cidades,
    fillvalue='Estado'
)
print(list(CidadeEstado))