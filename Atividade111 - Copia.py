class ControleRemoto:
    def __init__(self,cor,altura,profundidade,largura):
        self.cor=cor
        self.altura=altura
        self.profundidade=profundidade
        self.largura=largura 
        
        def mudar_canal (self,botao):
            if botao=="+":
                print("aumentar canal ")
            elif botao=="-":
                print("diminuir canal")
            else: 
                print("invalido")


controleremoto=ControleRemoto("","","","")

print (input("GGGGR",controleremoto.cor))
print(input(controleremoto.altura))
print(input(controleremoto.profundidade))
print(input(controleremoto.largura))

#cotrole01 = ControleRemoto  ()
#print(cotrole01.cor)