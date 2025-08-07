from random import randint
numero = randint(0, 5)

n = int(input("Insira o número. "))
if n < 0 or n > 5:
    print("Esse número não entra no jogo! Tente novamente.")
    exit()
if numero == n:
    print("Parabéns! Você acertou.")
else:
    print(f'O Python escolheu o número {numero}')
    print("Você errou! Tente novamente. ")
