n1 = int(input("Qual é a primeira nota? "))
n2 = int(input("Qual é a segunda nota? "))
media = (n1 + n2) / 2
if media < 50:
    print("Aluno reprovado. ")
if media > 50 and media < 70:
    print("Aluno satisfeito. ")
if media >= 70:
    print ("Parabéns! Aluno aprovado. ")

