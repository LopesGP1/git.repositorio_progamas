#16) [DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um 
#fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele 
#já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule 
#quantos dias de vida um fumante perderá e exiba o total em dias.
minutos =10
minutosPerd = 10
quantPorDia = float (input("Quantos sigarros você fuma por dia : "))
quantidadeAnofum = float(input("Digite quantos anos que já fuma:"))
totalMinutoPerd =quantPorDia*minutosPerd*365*quantidadeAnofum
diasPerdi = totalMinutoPerd / (60 * 24)
print (f"Você perdeu aproximadamente {diasPerdi:.2f} dias de vida.")



