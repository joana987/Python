altura = float(input("Quanto é que mede de altura? "))
peso = float(input("Quanto é que pesa? "))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'O seu IMC é {imc}, por isso você está abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print(f'O seu IMC é {imc}, por isso você está dentro do peso.')
else:
    print(f'O seu IMC é {imc}, por isso você está sobre o peso.')
