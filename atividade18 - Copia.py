#18) Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idades
#dela e depois mostre se ela pode ou não votar.
AnoNaci = int(input("Digite somento seu ano de nascimento :"))
AnoAT = int(input("Agora digite o ano atual :"))
Idade =AnoAT- AnoNaci
if Idade>= 18 :
    print("Você ja tem acima de {Idade} anos ja pode votar ")
elif Idade>=16 and Idade <18:
    print("Já pode votar mais ainda não e obrigatório so aparti dos 18 anos")
else :
    print("você tem menos que 18 anos não e obrigatório votar  ")
    