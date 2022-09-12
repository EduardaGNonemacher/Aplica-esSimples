# Todos os Produtos que custarem acima de 1.000 Dolares, imposto de 50% sobre o valor total

ListPrice = [50, 1500, 2000, 100, 25]

Imposto = [preco * 0.5 for preco in ListPrice if preco > 1000]

print(Imposto)
