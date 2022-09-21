from Dados import Produtos

def AumentarPreço(Preços):
    Preços['Preço'] = round(Preços['Preço'] * 1.05, 2) #setar casas decimais
    return Preços

NewPrices = map(AumentarPreço, Produtos) #mapear funções

for Produtos in NewPrices:
    print(Produtos)

#Aumentar preços sem mudar a estrutura original