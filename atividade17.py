#17) Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse
#80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba
#o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.
velociCar = float(input("Digite quan foi sua velociade pelo trajeto :"))
if velociCar <= 80:
    print("Voce esta dentro da velocidade limite ")
else:
    valor = 5*(velociCar-80)  
    print(f"O valor da multa e de {valor:.2f} R$")  


