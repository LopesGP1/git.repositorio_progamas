#20) Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ou
#ÍMPAR.
numer= int (input("Digite um numero inteiro  e o sistema vai indentificar se a par ou impar : "))
PI=numer%2
if PI== 0:
    print ("Esse numero e Par ")
else:
    print("Esse numero e Impar")