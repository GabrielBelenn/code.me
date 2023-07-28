#Escreva uma programa que calcula a média das notas de todos os alunos.
# Alunos e suas respectivas notas

alunos = [
("Alice", 8),
("Bob", 7),
("Carlos", 9)
]

soma = 0
quantidade = len(alunos)

for i in alunos:
   soma = soma + i[1]
   media = soma / quantidade
print("A média dos alunos foi de:", media, end=("."))
    
    

    

