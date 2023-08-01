#Implemente uma função que recebe dois argumentos, uma lista e um elemento , e
#retorna True caso elemento seja encontrado na lista , e False caso contrário. Não
#é permitido utilizar o método in.


lista_compras = ['banana', 'laranja', 'maçã', 'limao']
item_procurado = 'laranja'


def checar_lista(lista_compras, item_procurado):
    tamanho_lista = len(lista_compras)
    i = 0
    while i < tamanho_lista:
        if lista_compras[i] == item_procurado:
            return item_procurado
        i += 1
    return "Não encontrei o item pedido."

resultado = checar_lista(lista_compras, item_procurado)
print(resultado)

