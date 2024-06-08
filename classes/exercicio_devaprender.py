
class Carro:
    def __init__(self, marca, ano, modelo):
        self.marca = marca
        self.ano = ano
        self.modelo = modelo

    def ligar(self):
        print('ligando carro')

    def desligar(self):
        print('desligando carro')

    def andar(self):
        print('andando com o carro')

    def info(self):
        print(self.marca, self.ano, self.modelo)


carro1 = Carro('ford', '1998', 'ka')
carro1.ligar()
carro1.andar()
carro1.desligar()
carro1.info()