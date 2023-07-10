def main():
    x = int(input("Impar ou par, digite um numero: "))
    if for_par(x):
        print("Seu numero é par")
    else:
        print("Seu numero é impar")


def for_par(n):
    if n % 2 == 0:
        return True 
    else:
        return False 
    

main()