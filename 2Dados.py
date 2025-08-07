from random import randint
dado1 = 1
dado2 = 2
contagem = 0
while dado1 != dado2:
    dado1 = randint(0, 6)
    dado2 = randint(0, 6)
    contagem = contagem + 1
print(f'Foram precisas {contagem} jogadas.')
