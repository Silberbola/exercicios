#Aluno: Alexandre Silberstein
""" Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

Escreva um código que imprima todos os números exceto o número 13.
Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.

Como desafio, imprima eles em ordem decrescente (20, 19, 18...)
 """
 #Modo 1

for i in range(1, 21, 1):
    if i == 13:
        continue
    print("%dº andar" %i)

#Modo 2

andar = 0
while andar <= 19:
    andar +=1
    if andar == 13:
        continue
    print("%dº andar" %andar)

#Modo 3

andar = 1
for andar in range(100):
    andar +=1
    if andar == 13:
        continue
    if andar == 21:
        break
    print("%dº andar" %andar)


#Decrescente

for i in range(20, 0, -1):
    if i == 13:
        continue
    print("%dº andar" %i)
