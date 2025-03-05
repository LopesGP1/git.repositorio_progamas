# Atividade 1 classe pessoa 

class Pessoa:
    def __init__(self,nome,idade,endereco):
        self.nome = nome
        self.idade= idade 
        self.endereco = endereco
    def altera_dados(self,alterar):
        alterar = "s"
        if alterar=="s":
            Pessoa.nome = print(input("Digite seu nome : "))
            Pessoa.idade = print(input("Digite sua idade : "))
            Pessoa.endereco = print(input("Digite seu endereco : "))
        else:
            print("")

Pessoa.altera_dados(self,alterar)
pessoa_dados = Pessoa  ("Gabriel",17,"estancia")  
print (pessoa_dados.nome)  
print (pessoa_dados.idade)  
print (pessoa_dados.endereco)

#Pessoa.altera_dados()
resposta = print(input("Deseja alterar os dados digite 's' ou 'n' "))

if resposta== "s":
    alterar= resposta
    Pessoa.altera_dados(Self)

    