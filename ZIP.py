from itertools import zip_longest, count

Indice = count()
Cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Outros']
Estados = ['SP', 'MG', 'BA']

CidadesEstados = zip(
    Indice,
    Estados,
    Cidades
)

for Indice, Estados, Cidades in CidadesEstados:
    print(Indice, Estados, Cidades)