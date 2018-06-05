from PPlay.sprite import *
from Soldado import draw_soldados
from set_up import Personagens

class Enfermeira:

    def __init__(self, janela):
        self.janela = janela
        self.teclado = self.janela.get_keyboard()

        self.objeto = Sprite(Personagens.enfermeira)
        self.largura = self.objeto.width
        self.altura = self.objeto.height
        self.x = (janela.width / 2) - (self.largura / 2)
        self.y = (janela.height / 2) - (self.altura / 2)
        self.objeto.set_position(self.x, self.y)
        self.vel_x = 0
        self.vel_y = 0
        self.direcao = 1
        self.status = True

    def colisao(self, soldado):
        if soldado.y > self.y > soldado.y - (soldado.largura/2) and \
                self.teclado.key_pressed("SPACE"):

            if soldado.x < self.janela.width / 2:

                if self.x <= soldado.x + soldado.largura:
                    return True
            elif self.x >= soldado.x - soldado.largura:
                return True

    def mover(self, enfermeira_direita, enfermeira_esquerda, soldados,
              teclado, inicio, fim, espacos_entre_camas, espacos_camas):
        soldados_esquerda_x_fim = soldados[0].objeto.x + soldados[0].largura
        soldados_direita_x = soldados[1].objeto.x

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

        # Lado esquerdo
        if self.objeto.x > soldados_esquerda_x_fim - 10:
            move_esquerda(self, teclado)
        else:
            if not em_intervalo(self.objeto.y + self.altura, espacos_camas)[0]:
                if self.objeto.x > 0:
                    move_esquerda(self, teclado)

        # Lado direito
        if self.objeto.x + self.largura < soldados_direita_x + 10:
            move_direita(self, teclado)
        else:
            if not em_intervalo(self.objeto.y + self.altura, espacos_camas)[0]:
                if self.objeto.x + self.largura <= self.janela.width:
                    move_direita(self, teclado)

        # Move verticalmente
        if self.objeto.x > soldados_esquerda_x_fim - 10 and self.objeto.x + self.largura < soldados_direita_x + 10:
            move_verticalmente(self, teclado, inicio, fim)
        else:
            (v, x) = em_intervalo(self.objeto.y + self.altura, espacos_entre_camas)
            if v:
                move_verticalmente(self, teclado, x[0], x[1])

    def verifica_status(self, barra_sono, barra_fome, hud):
        if barra_fome.objeto.width < 0 or\
            barra_sono.objeto.width < 0 or\
                (hud.status_inimigos / 2) > hud.status_aliados:
            self.status = False


class EnfermeiraDireita:

    def __init__(self, largura_janela, altura_janela):

        self.objeto = Sprite(Personagens.enfermeira)
        self.largura = self.objeto.width
        self.altura = self.objeto.height
        self.x = (largura_janela / 2) - (self.largura / 2)
        self.y = (altura_janela / 2) - (self.altura / 2)
        self.objeto.set_position(self.x, self.y)

    def draw(self):
        self.objeto.draw()


class EnfermeiraEsquerda:

    def __init__(self, largura_janela, altura_janela):

        self.objeto = Sprite(Personagens.enfermeira_esq)
        self.largura = self.objeto.width
        self.altura = self.objeto.height
        self.x = (largura_janela / 2) - (self.largura / 2)
        self.y = (altura_janela / 2) - (self.altura / 2)
        self.objeto.set_position(self.x, self.y)

    def draw(self):
        self.objeto.draw()


def move_verticalmente(enfermeira, teclado, inicio, fim):
    if enfermeira.objeto.y + enfermeira.altura >= inicio:
        if teclado.key_pressed("up") or teclado.key_pressed("w"):
            enfermeira.y -= 1*enfermeira.vel_y
            enfermeira.objeto.move_y(- enfermeira.vel_y)
    if enfermeira.objeto.y + enfermeira.altura <= fim:
        if teclado.key_pressed("down") or teclado.key_pressed("s"):
            enfermeira.y += 1 * enfermeira.vel_y
            enfermeira.objeto.move_y(enfermeira.vel_y)


def move_cima(enfermeira, teclado, fim):
    if enfermeira.objeto.y > fim:
        if teclado.key_pressed("up") or teclado.key_pressed("w"):
            enfermeira.y -= 1 * enfermeira.vel_y
            enfermeira.objeto.move_y(- enfermeira.vel_y)


def move_baixo(enfermeira, teclado, fim):
    if enfermeira.objeto.y < fim:
        if teclado.key_pressed("down") or teclado.key_pressed("s"):
            enfermeira.y += 1 * enfermeira.vel_y
            enfermeira.objeto.move_y(enfermeira.vel_y)


def move_direita(enfermeira, teclado):
    if teclado.key_pressed("right") or teclado.key_pressed("d"):
        enfermeira.x += 1 * enfermeira.vel_x
        enfermeira.objeto.move_x(enfermeira.vel_x)
        enfermeira.direcao = 1


def move_esquerda(enfermeira, teclado):
    if teclado.key_pressed("left") or teclado.key_pressed("a"):
        enfermeira.x -= 1 * enfermeira.vel_x
        enfermeira.objeto.move_x(- enfermeira.vel_x)
        enfermeira.direcao = -1


def em_intervalo(x, lista_tuplas):
    for i in lista_tuplas:
        if i[0] <= x <= i[1]:
            return True, i
    return False, [0, 0]
