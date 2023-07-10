quantidade_de_itens = int(input("Quantidade de Itens: "))
valor_compras = float(input("Valor: "))
desconto = float(input("desconto: "))

print(f'O valor final será de R${valor_compras-desconto}, já considerando o desconto de R${desconto}')

print(f'O custo médio de cada item foi de R${(valor_compras-desconto)/quantidade_de_itens}')