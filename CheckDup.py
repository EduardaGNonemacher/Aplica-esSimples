
#Verificar se existem numeros repetidos na lista

ListIntInt = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 80],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 70],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 90],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]
def FirstDup(ForListInt):
    NumChecks = set()
    FirstDup = -1 #Retornar -1 se não houver numeros duplicados

    for Num in ForListInt:
        if Num in NumChecks:
            FirstDup = Num
            break

        NumChecks.add(Num)

    return FirstDup

for ListInt in ListIntInt:
    print(ListInt, FirstDup(ListInt))





