#Adapte a função maior_idade(pessoa) de forma que ela possa receber tanto uma
#tupla quanto um dicionário. Dica: método type pode te ajudar.

def maior_de_idade(cadastro):
    if isinstance(cadastro, tuple):
        nome, idade = cadastro  
    
    elif isinstance(cadastro, dict):
        nome = cadastro.get('nome')
        idade = cadastro.get('idade') 
    
    if idade >= 18:
        return f"{nome} é maior de idade."
    else:
        return f"{nome} é menor de idade."


cadastro = {'nome': 'Amanda', 'idade': 18}  
resultado = maior_de_idade(cadastro)
print(resultado)

