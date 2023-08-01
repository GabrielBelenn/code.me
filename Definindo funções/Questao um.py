#Escreva uma função que recebe um número inteiro positivo e retorna True caso ele
#seja primo e False , caso contrário.


def e_primo(n): #numeros primos sao divisiveis no máximo duas vezes.
    if n <= 1:
        return False
    numero_de_divisores = 0 
    for i in range(1, n + 1):
        if n % i == 0:
            numero_de_divisores += 1
        if numero_de_divisores >= 3:
            return False
    return True
        
        
print(e_primo(1))

print(e_primo(2))