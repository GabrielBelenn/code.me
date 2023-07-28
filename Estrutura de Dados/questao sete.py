#Escreva um programa que solicite uma string para o usuário e imprima quantas
#vezes cada letra aparece na palavra.
dic = {

}

palavra = input('Digite uma palavra: ').lower()
letras_repetidas = '' 

print('A sua palavra tem {} letras ao todo'.format(len(palavra)), end=".\n")

for letra in palavra:
    if letra not in letras_repetidas:
        letras_repetidas += letra
    
for letra in letras_repetidas:
    dic[letra] = palavra.count(letra)

for chave, valor in dic.items():
    print(f"{chave}: {valor}")
    

    

    
