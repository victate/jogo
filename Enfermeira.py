from PPlay.sprite import *


class Enfermeira:

    def __init__(self, janela):
        self.janela = janela
        self.objeto = Sprite("images/enfermeira.png")
        self.largura = self.objeto.width
        self.altura = self.objeto.height
        self.objeto.set_position(
            (janela.width / 2) - (self.largura / 2),
            (janela.height / 2) - (self.altura / 2)
        )
        self.vel_x = 0
        self.vel_y = 0
        self.direcao = 1

    def mover(self, enfermeira_direita, enfermeira_esquerda, soldados, teclado, inicio, fim):
        # Muda de sprite de acordo com a direção
        self.vel_x = 100 * self.janela.delta_time()
        self.vel_y = 80 * self.janela.delta_time()
        if self.direcao > 0:
            enfermeira_direita.objeto.x, enfermeira_direita.objeto.y = self.objeto.x, self.objeto.y
            draw_soldados(soldados, enfermeira_direita)

        else:
            enfermeira_esquerda.objeto.x, enfermeira_esquerda.objeto.y = self.objeto.x, self.objeto.y
            draw_soldados(soldados, enfermeira_esquerda)

        # Move horizontalmente
        if self.objeto.x > 0:
            if teclado.key_pressed("left"):
                self.objeto.move_x(- self.vel_x)
                self.direcao = -1
        if self.objeto.x < self.janela.width - self.largura:
            if teclado.key_pressed("right"):
                self.objeto.move_x(self.vel_x)
                self.direcao = 1

        # Move verticalmente
        if self.objeto.y > inicio:
            if teclado.key_pressed("up"):
                self.objeto.move_y(- self.vel_y)
        if self.objeto.y < fim:
            if teclado.key_pressed("down"):
                self.objeto.move_y(self.vel_y)


class EnfermeiraDireita:

    def __init__(self, largura_janela, altura_janela):
        self.objeto = Sprite("images/enfermeira.png")
        self.largura = self.objeto.width
        self.altura = self.objeto.height
        self.objeto.set_position(
            (largura_janela / 2) - (self.largura / 2),
            (altura_janela / 2) - (self.altura / 2)
        )

    def draw(self):
        self.objeto.draw()


class EnfermeiraEsquerda:

    def __init__(self, largura_janela, altura_janela):
        self.objeto = Sprite("images/enfermeira_esquerda.png")
        self.largura = self.objeto.width
        self.altura = self.objeto.height
        self.objeto.set_position(
            (largura_janela / 2) - (self.largura / 2),
            (altura_janela / 2) - (self.altura / 2)
        )

    def draw(self):
        self.objeto.draw()


def draw_soldados(lista, enfermeira):
    i = 0
    while lista[i].objeto.y < enfermeira.objeto.y:
        lista[i].objeto.draw()
        i += 1
        if i == len(lista):
            break
    enfermeira.objeto.draw()
    for j in range(i, len(lista)):
        lista[j].draw()
