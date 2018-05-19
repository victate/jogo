from PPlay.sprite import *


class Enfermeira:

    def __init__(self, janela):
        self.janela = janela
        self.teclado = janela.get_keyboard()
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

    def mover(self, enfermeira_direita, enfermeira_esquerda, soldados,
              inicio, fim, espacos_entre_camas, espacos_camas):
        soldados_esquerda_x_fim = soldados[0].objeto.x + soldados[0].largura
        soldados_direita_x = soldados[1].objeto.x

        # Muda de sprite de acordo com a direção
        self.vel_x = 200 * self.janela.delta_time()
        self.vel_y = 100 * self.janela.delta_time()
        if self.direcao > 0:
            enfermeira_direita.objeto.x, enfermeira_direita.objeto.y = self.objeto.x, self.objeto.y
            draw_soldados(soldados, enfermeira_direita)
        else:
            enfermeira_esquerda.objeto.x, enfermeira_esquerda.objeto.y = self.objeto.x, self.objeto.y
            draw_soldados(soldados, enfermeira_esquerda)

        # Move horizontalmente

        # Lado esquerdo
        if self.objeto.x < soldados_esquerda_x_fim - 10:
            x, (a, b) = em_intervalo(self.objeto.y + self.altura, espacos_camas)
            if self.objeto.x > 0:
                if not x:
                    move_esquerda(self, self.teclado)
        else:
            move_esquerda(self, self.teclado)

        # Lado direito
        if self.objeto.x + self.largura > soldados_direita_x + 10:
            x, (a, b) = em_intervalo(self.objeto.y + self.altura, espacos_camas)
            if self.objeto.x + self.largura < self.janela.width:
                if not x:
                    move_direita(self, self.teclado)
        else:
            move_direita(self, self.teclado)

        # Move verticalmente
        if self.objeto.x > soldados_esquerda_x_fim - 10 and \
                self.objeto.x + self.largura < soldados_direita_x + 10:
            move_verticalmente(self, self.teclado, inicio, fim)
        else:
            (v, x) = em_intervalo(self.objeto.y + self.altura, espacos_entre_camas)
            if v:
                move_verticalmente(self, self.teclado, x[0], x[1])


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
    # Desenha os Soldados
    while lista[i].objeto.y < enfermeira.objeto.y:
        lista[i].draw()
        i += 1
        if i == len(lista):
            break
    # Desenha a Enfermeira
    enfermeira.objeto.draw()
    # Desenha o resto dos Soldados
    for j in range(i, len(lista)):
        lista[j].draw()


def move_verticalmente(enfermeira, teclado, inicio, fim):
    if enfermeira.objeto.y + enfermeira.altura > inicio:
        if teclado.key_pressed("up"):
            enfermeira.objeto.move_y(- enfermeira.vel_y)
    if enfermeira.objeto.y + enfermeira.altura < fim:
        if teclado.key_pressed("down"):
            enfermeira.objeto.move_y(enfermeira.vel_y)


def move_cima(enfermeira, teclado, fim):
    if enfermeira.objeto.y > fim:
        if teclado.key_pressed("up"):
            enfermeira.objeto.move_y(- enfermeira.vel_y)


def move_baixo(enfermeira, teclado, fim):
    if enfermeira.objeto.y < fim:
        if teclado.key_pressed("down"):
            enfermeira.objeto.move_y(enfermeira.vel_y)


def move_direita(enfermeira, teclado):
    if teclado.key_pressed("right"):
        enfermeira.objeto.move_x(enfermeira.vel_x)
        enfermeira.direcao = 1


def move_esquerda(enfermeira, teclado):
    if teclado.key_pressed("left"):
        enfermeira.objeto.move_x(- enfermeira.vel_x)
        enfermeira.direcao = -1


def em_intervalo(x, lista_tuplas):
    for i in lista_tuplas:
        if i[0] <= x <= i[1]:
            return True, i
    return False, [0, 0]
