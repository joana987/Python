salario = int(input("Qual é o seu salário atual? "))
if salario < 500:
    print(f'O seu novo salário será, {salario + (salario * 0.15)}')
elif salario < 1000:
    print(f'O seu novo salario será, {salario + (salario * 0.10)}')
else:
    print(f'O seu novo salário será, {salario + (salario * 0.05)}')
