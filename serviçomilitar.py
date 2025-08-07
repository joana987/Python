from datetime import date
ano_atual = date.today().year
ano = int(input("Em que ano nasceu? "))
idade = (ano_atual - ano)
print(f'Você tem {idade} anos.')
if idade < 18:
    print("Ainda não tens idade para o recenseamento.")
elif idade >= 18 and idade <= 25:
    print("Está no momento para o recenseamento.")
else:
    print("Já passou o prazo para o recenseamento.")
