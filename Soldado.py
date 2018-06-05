
from PPlay.gameimage import *
from geradores_random import gerar_prontuario
from set_up import Personagens, Objetos


class SoldadoEsquerda:

    def __init__(self, janela, posicao_y):
        self.janela = janela
        self.objeto = GameImage(Personagens.soldado_esq)
        self.maca = GameImage(Objetos.maca_esq)

        self.largura = self.objeto.width
        self.altura = self.objeto.height

        self.x = 10
        self.y = posicao_y

        self.objeto.set_position(self.x, self.y)
        self.maca.set_position(self.x, self.y)

        # False se soldado curado
        self.status = True
        self.prontuario = gerar_prontuario()

    def draw_soldado(self):
        self.objeto.draw()

    def draw_maca(self):
        self.maca.draw()


class SoldadoDireita:

    def __init__(self, janela, posicao_y):
        self.janela = janela
        self.objeto = GameImage(Personagens.soldado)
        self.maca = GameImage(Objetos.maca_dir)

        self.largura = self.objeto.width
        self.altura = self.objeto.height

        self.x = janela.width - self.largura - 10
        self.y = posicao_y

        self.objeto.set_position(self.x, self.y)
        self.maca.set_position(self.x, self.y)

        # False se soldado curado
        self.status = True
        self.prontuario = gerar_prontuario()

    def draw_soldado(self):
        self.objeto.draw()

    def draw_maca(self):
        self.maca.draw()


def draw_soldados(lista, enfermeira):
    i = 0
    while lista[i].objeto.y < enfermeira.objeto.y:
        if lista[i].status:
            lista[i].draw_soldado()
        else:
            lista[i].draw_maca()
        i += 1
        if i == len(lista):
            break
    enfermeira.objeto.draw()
    for j in range(i, len(lista)):
        if lista[j].status:
            lista[j].draw_soldado()
        else:
            lista[j].draw_maca()


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
