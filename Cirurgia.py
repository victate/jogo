from PPlay.gameimage import *


class Cirurgia:

    def __init__(self, janela):
        self.janela = janela

        self.objeto = GameImage("images/cirurgia.png")

        self.largura = self.objeto.width
        self.altura = self.objeto.height
        self.objeto.set_position(
            (self.janela.width / 2) - (self.largura / 2), 5
        )

    def draw(self):
        self.objeto.draw()
