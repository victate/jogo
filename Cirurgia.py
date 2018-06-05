from PPlay.gameimage import *
from set_up import Objetos

class Cirurgia:

    def __init__(self, janela):
        self.janela = janela

        self.objeto = GameImage(Objetos.cirurgia)

        self.largura = self.objeto.width
        self.altura = self.objeto.height
        self.objeto.set_position(
            (self.janela.width / 2) - (self.largura / 2), 5
        )
        self.ocupado = False

    def draw(self):
        self.objeto.draw()

    def receber_paciente(self, soldado):
        self.ocupado = True

    def liberar_paciente(self, soldado):
        self.ocupado = False

    def get_ocupacao(self):
        return self.ocupado
