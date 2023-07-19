# Um número primo é um número que é divisível apenas por 1 e por ele mesmo. 
#Escreva um programa que receba um número n e informe se esse número é primo ou não.

n = " "
i = 1 
total = 0

n = int(input("Digite um numero: "))
while i <= n:
    if n % i == 0:
        total += 1
    i += 1
if total  == 2:
    print("Este numero é primo!")
else:
    if total > 2:
        print("Este numero não é primo!")        