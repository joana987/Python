velocidade = int(input("Qual é a velocidade do carro ao passar pelo radar? "))
if velocidade <= 80:
    print("Estás dentro do limite. Boa viagem!")
if velocidade > 80:
    x = velocidade - 80
    multa = x * 2
    print(f'Estás acima do limite permitido. A multa vai ser gerada no valor de {multa} euros!')


