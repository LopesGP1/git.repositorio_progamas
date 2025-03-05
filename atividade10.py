#10) Faça um algoritmo que leia a largura e altura de uma parede, calcule e 
#mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, 
#sabendo que cada litro de tinta pinta uma área de 2metros quadrados
print ("Vamos calcular quanto de tinta será nessesario para um parede ")
altura=float(input("Digite a altura da parede :"))
largura = float(input("Digite a largura da parede :"))
area = altura*largura 
tinta = area/2
print("A quantia de tinta e de ",tinta )