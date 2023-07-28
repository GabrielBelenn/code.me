# Alunos e suas notas representados através de dicionários
#Escreva uma programa que calcula a média das notas de todos os alunos.

alunos = [
{
"nome": "Alice",
"nota": 8,
},
{
"nome": "Bob",
"nota": 7,
},
{
"nome": "Carlos",
"nota": 9,
}
]

soma = 0 
quantidade = len(alunos)

for aluno in alunos:
    soma = soma + aluno["nota"]
    media = soma / quantidade 

print("A média da soma de todos os alunos é:", media, end=".")



