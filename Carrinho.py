Car = []

Car.append(('Produto 1', 30))
Car.append(('Produto 2', 20))
Car.append(('Produto 3', 50))

Total = sum([float(y) for x, y in Car])
print(Car)
print(f'O Total dos Produtos é {Total}')