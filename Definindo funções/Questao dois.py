#Implemente uma função que recebe uma lista de números inteiros e retorna uma
#tupla (pos, num) , onde pos é a posição (ou índice) do maior número na lista e num
#é o valor desse número.

lista = [1,19,8,22,30,15]


def tupla_valor_posicao(lista):
    maior_numero = lista[0]
    maior_posicao = 0
    
    for i, num in enumerate(lista):
        if num > maior_numero:
            maior_numero = num
            maior_posicao = i
    return maior_numero, maior_posicao


resultado = tupla_valor_posicao(lista)
print(resultado)