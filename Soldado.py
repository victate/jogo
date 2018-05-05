from PPlay.gameimage import *


class SoldadoEsquerda:

    def __init__(self, janela, posicao_y):
        self.objeto = GameImage("images/soldado_esquerda.png")
        self.largura = self.objeto.width
        self.altura = self.objeto.height
        self.objeto.set_position(15, posicao_y)

    def draw(self):
        self.objeto.draw()


class SoldadoDireita:

    def __init__(self, janela, posicao_y):
        self.objeto = GameImage("images/soldado_direita.png")
        self.largura = self.objeto.width
        self.altura = self.objeto.height
        self.objeto.set_position(
            janela.width - self.largura - 15, posicao_y
        )

    def draw(self):
        self.objeto.draw()