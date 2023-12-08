class Carro:

  def __init__(self, cor, marca, modelo, ligado=False, andando= False):

      self.cor = cor
      self.marcar = marca
      self.modelo = modelo
      self.ligado = False
      self.andando = False

  def ligar(self):
      if self.ligado:
        print('o carro ja esta ligado')
        return

      print('Ligado')
      self.ligado = True 

  def desligar(self):
      if not self.ligado:
        print('o carro ja esta desligado')
        return 
      print('desligado')
      self.ligado = False
  
  def andar(self):
      if self.ligado == False:
        print('é preciso ligar o carro primeiro!')
        return

      print('esta andando')
      self.andando = True

  def parar(self):
      if not self.andando:
        print('o carro ja esta parado!')
        return

      print('parado!')  
      self.andando = True

  def status_motor(self):
      if self.ligado == True: 
        print(f'o motor esta ligado?:{self.ligado} ')
      else:
        print(f'o motor esta ligado?: {self.ligado}')

  


      


c = Carro("cor","marca","modelo")
c.ligar()
c.andar()
c.parar()
c.desligar()


print(c.status_motor())
