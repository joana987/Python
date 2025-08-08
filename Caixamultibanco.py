nota5 = 0
nota10 = 0
nota20 = 0
nota50 = 0
nota100 = 0
dinheiro = int(input("Quanto dinheiro é que quer levantar? "))
if dinheiro % 5 != 0 or 5 > dinheiro or dinheiro > 1000:
    dinheiro = int(input("Esse número é inválido. Tente colocar outro."))
while dinheiro > 0:
    print("Primeiro loop")
    if dinheiro >= 100:
        print("Primeiro if")
        nota100 = nota100 + 1
        dinheiro = dinheiro - 100
    elif dinheiro >= 50:
        nota50 = nota50 + 1
        dinheiro = dinheiro - 50
    elif dinheiro >= 20:
        nota20 = nota20 + 1
        dinheiro = dinheiro - 20
    elif dinheiro >= 10:
        nota10 = nota10 + 1
        dinheiro = dinheiro - 10
    elif dinheiro >= 5:
        nota5 = nota5 + 1
        dinheiro = dinheiro - 5
print(f'Vai receber {nota100} notas de 100€, {nota50} notas de 50€, {nota20} notas de 20€, {nota10} notas de 10€ e {nota5} notas de 5€.')
