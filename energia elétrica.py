kWh = int(input("Qual é a quantidade de kWh consumida? "))
tipo = input("Qual é o tipo de instalação? ")
if tipo == "R":
    if kWh < 500:
        print(f'O preço é {kWh * 0.40}€')
    else:
        print(f'O preço é {kWh * 0.65}€')
if tipo == "C":
    if kWh <1000:
        print(f'O preço é {kWh * 0.55}€')
    else:
        print(f'O preço é {kWh * 0.60}€')
if tipo == "I":
    if kWh <5000:
        print(f'O preço é {kWh * 0.55}')
    else:
        print(f'O preço é {kWh * 0.60}')
