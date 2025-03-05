#14) A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva 
#um programa que pergunte a quantidade de Km percorridos por um carro alugado e a 
#quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar, 
#sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.
diaAluga= 90
kmRodados = 0.20
n1 = float(input("Digite quantos dias foi alugado o carro :"))
n2 = float(input("Digite quantos km foram rodados : "))
valorToda= (diaAluga*n1)+(kmRodados*n2)
print(f"O valor total do carro aluga foi de :{valorToda:.2f} R$" )
