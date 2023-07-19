# Escreva um programa que receba um número inteiro n e imprima a soma de todos os números de 1 até n (inclusive n ).

n = int(input("Digite um número: "))
i = 1 
soma = 0

while i <= n:
    i = i + 1
    soma = soma + i
    print(soma + 1)
