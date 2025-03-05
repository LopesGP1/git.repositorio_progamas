#31) [DESAFIO] Crie um jogo de JoKenPo (Pedra-Papel-Tesoura)
import time
import os 
#time.sleep(0.7)
os.system("cls")
#os.sytem('cls')#para windows
time.sleep(1.0)
print ("Bem vindo ao jogo JoKenPo ")
time.sleep(1.0)
print("Vamos começar!?")
time.sleep(2.3)
os.system("cls")
nome = input("Digite seu nome :")

opcoes = {1: "pedra", 2: "papel", 3: "tesoura"}


time.sleep(0.9)
s = "s"
while s == "s":
    
    print("Voce irá jogar contra um robô que vai escolher entre três opcoes que é pedra, papel e tesoura ")
    time.sleep(0.9)
    print("pedra é 1")
    pedra = 1
    print("papel é 2")
    time.sleep(0.9)
    papel =2
    print("tesoura é 3")
    tesoura=3
    escolhaJogador = int(input("Digite qual vai ser sua opção :"))
    print("O robó irá escolher agora ")
    time.sleep(0.5)
    print(".",end="" )
    time.sleep(0.5)
    print(".",end="" )
    time.sleep(0.5)
    print(".",end="" )
    time.sleep(3.3)
    os.system("cls")
    import random
    numero_aleatorio = random.randint(1,3)
    if escolhaJogador == numero_aleatorio:
            
            print("Deu empate!")
            print(f"{nome} escolheu {opcoes[escolhaJogador]} e o robô escolheu {opcoes[numero_aleatorio]}.")
    elif (escolhaJogador == 1 and numero_aleatorio == 3) or (escolhaJogador == 2 and numero_aleatorio == 1) or (escolhaJogador == 3 and numero_aleatorio == 2):
            
            print(f"Você escolheu {opcoes[escolhaJogador]} e o robô escolheu {opcoes[numero_aleatorio]}. Você ganhou!!!")
    else:
            print(f"Você escolheu {opcoes[escolhaJogador]} e o robô escolheu {opcoes[numero_aleatorio]}. Você perdeu!!!")
        
    s = input("Deseja repetir? (s/n): ")
    #os.sytem("cls")


