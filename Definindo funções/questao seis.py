# Uma função fatorial calcula o valor da multiplicação de um certo número inteiro não-negativo por 
# todos os números positivos menores que ele. A exceção é o fatorial de zero que é igual a 1.
# Implemente a função fatorial(n) de modo que ela retorne o valor do fatorial de n:

n = int(input("Digite um numero: ")) 
i = 2 
fat = 1 


def calculadora_fatorial(n, i, fat):    
    while i <= n: 
        fat = fat * i 
        i = i + 1 
    return f"O resultado de {n}! é {fat}"


resultado = calculadora_fatorial(n, i, fat)
print(resultado)





        