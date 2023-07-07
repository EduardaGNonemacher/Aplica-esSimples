# O Objetivo do Exercicio é criar uma função que multiplica todos os argumentos não nomeados recebidos 

def Multi(*args):
    Total = 1 
    for número in args:
        Total *= número
        
    return Total 

Valor1 = Multi(80, 116)
print(Valor1)

################################################################################################################

# O Objetivo do segundo exercicio é criar uma função que nos informa se um número é par ou ímpar 

def par_impar(número):
    if número % 2 == 0:
        print(f'{número} é par')
    else:
        print(f'{número} é ímpar')
par_impar(80)

