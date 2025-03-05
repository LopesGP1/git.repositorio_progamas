#15) Crie um programa que leia o número de dias trabalhados em um mês e mostre o 
#salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25 
#por hora trabalhada
print("Vamos calcular quanto que você ganha no mês ")
diasTrab =int( input("Digite quantos dia você trabalhou no mês :"))
quantoHora= float(input ("digite quanto que você quanto por hora "))


precoDia =float((8*quantoHora)*diasTrab)
print(f"Seu salário fica {precoDia:.2f} R$")