ana = 0
bruno = 0
carla = 0
print("Aqui pode votar para o reality show: Digite 1 para votar na Ana. Digite 2 para votar no Bruno. Digite 3 para votar na Carla. Digite 0 parar a votação.")
while True:
    votacao = int(input("Digite aqui o número: "))
    if votacao == 1:
        print("Você votou na Ana.")
        ana = ana + 1
    elif votacao == 2:
        print("Você votou no bruno.")
        bruno = bruno + 1
    elif votacao == 3:
        print("Você votou na Carla")
        carla = carla + 1
    elif votacao == 0:
        break
    else:
        print("Voto inválido. Tente novamente. ")
print(f'Resultados: A Ana recebeu {ana} votos. O Bruno recebeu {bruno} votos. A Carla recebeu {carla} votos.')
if ana > bruno and ana > carla:
    print("A Ana obteu mais votos por isso é a vencedora.")
elif bruno > ana and bruno > carla:
    print("O Bruno obteu mais votos por isso é o vencedor.")
else:
    print("A Carla obteu mais votos por isso é a vencedora.")
