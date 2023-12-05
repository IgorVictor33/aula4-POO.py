class Carro:

    def __init__(self, cor, marca, modelo):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.ligado = False
        self.andando = False

    def ligar(self):
       if self.ligado == True:
         Print(motor , 'ligado!')
       else:
         print('desligado!')
       
    def desligar(self):
        if self.ligado == True:
            print(motor, 'desligado!')
    
    def andar(self):
        if self.andando == True:
            print(movimento, 'andando!')

    def parar(self):
        if self.andando == True:
            print(movimento, 'andando!')
        else:
            print(movimento, 'parado!')
    
    def status(self):
        motor ='motor esta: '
        movimento ='o carro esta: '

        return motor + ' ' + movimento

carro = Carro("cor", "marca", "modelo")
carro.ligar()
print(carro.status())

carro = Carro("cor", "marca", "modelo")
carro.desligar()
print(carro.status())


    
    


 