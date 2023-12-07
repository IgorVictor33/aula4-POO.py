class Carro:

    def __init__(self, cor, marca, modelo):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.ligado = False
        self.andando = False

    def ligar(self):
       if self.ligado == True:
        print(motor , 'ligado!')
       else:
        print('desligado!')
       if self.ligado == False:
        print('esta parado!')
       else:
        print('esta andando!')  
       

    def desligar(self):
       if self.ligado:
        print(f'o carro ja esta ligado!')

       if self.ligado == True:
        print(motor, 'desligado!')
        return

    
    def andar(self):

       if self.andando == True:
        print(movimento, 'andando!')
       if self.status == False:
        print(motor, 'esta ligado!')
        return


    def parar(self):

      if self.andando:
        print(movimento, 'andando!')
      return

      print(movimento, 'parado!')
      self.andando = False
    
    def status(self):
        motor = f'o motor esta ligado: ? {self.ligado}.' 
        
        
        movimento =f'o carro esta em movimento? {self.andando} '

        return motor + ' ' + movimento

carro = Carro("cor", "marca", "modelo")
carro.desligar()
print(carro.status())

carro.ligar()

    
    


 
