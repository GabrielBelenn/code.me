#Implemente uma função maior_idade(pessoa) que receba uma tupla representando
#uma pessoa com nome e idade e imprime na tela se a pessoa é maior de idade ou não.

def maior_de_idade(cadastro):
    nome, idade = cadastro  
    if idade >= 18:
        return f"{nome} é maior de idade."
    else:
        return f"{nome} é menor de idade."


cadastro = ("Amanda", 18)  
resultado = maior_de_idade(cadastro)
print(resultado)




