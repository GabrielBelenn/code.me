#Jogo “Acerte o número”


n = 8
i = " "
vezes = 0

print("Acerte o numero de 1 a 10, você terá três chances!")

while vezes < 3:
    
    i = int(input("-->"))
    if (i == n):
        print("Você acertou!")
        break
        
    elif i >= 11:
        print("Seu número está entre 1 e 10!")
        vezes += 1
    
    elif (i < n):
        print("Mais para cima!")
        vezes += 1
        
    elif (i > n):
        print("Mais para baixo!")
        vezes += 1

if vezes == 3:
    print("Você perdeu, tente novamente.")