from PPlay.gameimage import *
from geradores_random import gerar_prontuario

class SoldadoEsquerda:

    def __init__(self, janela, posicao_y):
        self.janela = janela
        self.objeto = GameImage("images/soldado_esquerda.png")
        self.largura = self.objeto.width
        self.altura = self.objeto.height
        self.x = 10
        self.y = posicao_y
        self.objeto.set_position(self.x, self.y)
        self.prontuario = gerar_prontuario()

    def draw(self):
        self.objeto.draw()


class SoldadoDireita:

    def __init__(self, janela, posicao_y):
        self.janela = janela
        self.objeto = GameImage("images/soldado_direita.png")
        self.largura = self.objeto.width
        self.altura = self.objeto.height
        self.x = janela.width - self.largura - 10
        self.y = posicao_y
        self.objeto.set_position(
            self.x, self.y)
        self.prontuario = gerar_prontuario()

    def draw(self):
        self.objeto.draw()


def espacos_entre_camas(soldados, inicio, fim):
    e = [(inicio, soldados[0].objeto.y + soldados[0].altura - 21)]
    j = 0
    for j in range(1, len(soldados) - 1, 2):
        e.append((soldados[j - 1].objeto.y + soldados[j - 1].altura + 14,
                  soldados[j + 1].objeto.y + soldados[j + 1].altura - 21))
    e.append((soldados[j + 1].objeto.y + soldados[j + 1].altura + 14, fim))
    return e


def espacos_camas(espacos_entre_camas):
    e = [(espacos_entre_camas[0][1], espacos_entre_camas[1][0])]
    for i in range(1, len(espacos_entre_camas) - 1):
        e.append((espacos_entre_camas[i][1], espacos_entre_camas[i + 1][0]))
    return e
