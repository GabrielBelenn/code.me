a = 0
b = 0
op = " "
resultado = 0
r = "S"

while r == "S":

    a = float(input("Digite um numero: "))
    op = input("Dige a operação (+, -, x, %): ")
    b = float(input("Digite outro numero: "))

    if op == "+":
        resultado = a + b
        print(str(a) + ' ' + str(op) + ' ' + str(b) + ' ' + "=" + ' ' + str(resultado))


    elif op == "-":
        resultado = a - b
        print(str(a) + ' ' + str(op) + ' ' + str(b) + ' ' + "=" + ' ' + str(resultado))


    elif op == "x":
        resultado = a * b
        print(str(a) + ' ' + str(op) + ' ' + str(b) + ' ' + "=" + ' ' + str(resultado))


    elif b != 0:
        resultado = a / b
        print(str(a) + ' ' + str(op) + ' ' + str(b) + ' ' + "=" + ' ' + str(resultado))
    
    elif b == 0:
        print("Não é possivel dividir por zero")

    else:
        print("Operação inválida")

    r = input("Deseja continuar?[S/N] ").upper()

