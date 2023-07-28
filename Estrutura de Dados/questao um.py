#Escreva um programa que lê números inteiros positivos do usuário, um após o
#outro, e monta uma lista a partir desses números e depois imprime a lista montada.
#O programa deve continuar solicitando por números até que o elemento digitado
#seja um número negativo (que não deve ser inserido na lista).

lista = []
numeros = " "


while numeros:
    numeros = int(input("Adcione um número a sua lista: "))
    lista.append(numeros)
    
    if numeros > 0:
        continue
    else:
        break

    
    
print(lista) 

                