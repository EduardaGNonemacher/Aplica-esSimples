from itertools import groupby, tee

Alunos = [
    {'Nome': 'Bigena', 'Nota': 'B'},
    {'Nome': 'Eduarda', 'Nota': 'A'},
    {'Nome': 'Thresh', 'Nota': 'D'},
    ]

Ordena = lambda Item: Item['Nota'] ##não precisa definir, ou seja, não vai precisar escrever a função e depois utilizá-la dentro do código.#
Alunos.sort(key=Ordena) ##classifica a lista em ordem crescente por padrão.#
AlunosAgrup = groupby(Alunos, Ordena)

for Agrupamento, ValAgrupados in AlunosAgrup:
    Val1, Val2 = tee(ValAgrupados)

    print(f'Agrupamento: {Agrupamento}')

    for Alunos in Val1:
        print(f'\t{Alunos}')

    Quant = len(list(Val2))
    print(f'\t{Quant} Alunos tiraram a nota {Agrupamento}')
    print()
