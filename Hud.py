from PPlay.gameimage import *
from PPlay.sprite import *
from set_up import Inventario, Display

class Hud:

    def __init__(self, janela):
        self.janela = janela

        self.objeto = GameImage(Display.fundo)

        self.largura = self.objeto.width
        self.altura = self.objeto.height
        self.objeto.set_position(
            (self.janela.width - self.largura) / 2,
            self.janela.height - self.altura - 10
        )
        self.status_aliados = 99
        self.status_inimigos = 99

    def draw(self):
        self.objeto.draw()
        self.janela.draw_text(str(self.status_aliados), self.objeto.x + self.largura - 120,
                              self.objeto.y + self.altura - 70, size=44, color=(0, 0, 0), bold=True)
        self.janela.draw_text("/" + str(self.status_inimigos), self.objeto.x + self.largura - 73,
                              self.objeto.y + self.altura - 64, size=35, color=(255, 0, 0), bold=True)


class Bandagem:

    def __init__(self, hud, janela):
        self.janela = janela
        self.hud = hud

        self.objeto = GameImage(Inventario.bandagens)
        self.largura = self.objeto.width
        self.altura = self.objeto.height
        self.objeto.set_position(
            (self.hud.largura / 5) + (self.largura / 2) + 10,
            self.hud.objeto.y + (self.hud.altura / 2) - self.altura + 40
        )
        self.qtd = 3

    def usar_bandagem(self):
        if(self.qtd > 0):
            self.set_qnt(self.qtd-1)
            return True
        return False

    def set_qnt(self, new_qnt):
        self.qtd = new_qnt

    def draw(self):
        self.janela.draw_text("x" + str(self.qtd), self.objeto.x + self.largura + 5,
                              self.objeto.y + self.altura - 35, size=35, color=(0, 0, 0))
        self.objeto.draw()


class Barras:

    def __init__(self, hud):
        self.hud = hud
        self.objeto = GameImage(Display.barras)
        self.largura = self.objeto.width
        self.altura = self.objeto.height
        self.objeto.set_position(
            (self.hud.largura / 2) - (self.largura / 2) + 75,
            self.hud.objeto.y + (self.hud.altura / 2) - (self.altura / 2)
        )

    def draw(self):
        self.objeto.draw()

    def dormir(barra_sono):
        barra_sono.aumenta_barra(50)

    def repor_inventario(penicilina, bandagem):
        penicilina.set_qnt(3)
        bandagem.set_qnt(3)

    def comer(barra_fome):
        barra_fome.aumenta_barra(50)


class BarraFome:

    def __init__(self, barras):
        self.objeto = Sprite(Display.barra_fome)
        self.largura = self.objeto.width
        self.objeto.width = 100

        self.intervalo_fome = 5000
        self.t_fome = 0

        self.x = self.objeto.x
        self.y = self.objeto.y
        self.objeto.set_position(barras.objeto.x + 3, barras.objeto.y + 3)

    def draw(self):
        self.objeto.draw()

    def aumenta_fome(self, tempo_atual):
        if tempo_atual - self.t_fome >= self.intervalo_fome:
            self.diminui_barra(5)
            self.t_fome = tempo_atual

    def aumenta_barra(self, tamanho):
        if self.objeto.width < self.largura:
            self.objeto.width += tamanho
        else:
            self.objeto.width = self.largura

    def diminui_barra(self, tamanho):
        if self.objeto.width > 0:
            self.objeto.width -= tamanho
        else:
            self.objeto.width = 0


class BarraSono:

    def __init__(self, barras):
        self.objeto = Sprite(Display.barra_sono)

        self.largura = self.objeto.width
        self.objeto.width = 100

        self.intervalo_sono = 11000
        self.t_sono = 0

        self.x = self.objeto.x
        self.y = self.objeto.y
        self.objeto.set_position(barras.objeto.x + 3, barras.objeto.y + (2*self.objeto.height) + 10)

    def draw(self):
        self.objeto.draw()

    def aumenta_sono(self, tempo_atual):
        if tempo_atual - self.t_sono >= self.intervalo_sono:
            self.diminui_barra(7)
            self.t_sono = tempo_atual

    def aumenta_barra(self, tamanho):
        if self.objeto.width < self.largura:
            self.objeto.width += tamanho
        else:
            self.objeto.width = self.largura

    def diminui_barra(self, tamanho):
        if self.objeto.width > 0:
            self.objeto.width -= tamanho
        else:
            self.objeto.width = 0


class Penicilina:

    def __init__(self, hud, janela):
        self.hud = hud
        self.janela = janela

        self.objeto = GameImage(Inventario.penicilina)
        self.largura = self.objeto.width
        self.altura = self.objeto.height
        self.objeto.set_position(
            (self.hud.largura / 40) + (self.largura / 2),
            self.hud.objeto.y + (self.hud.altura / 2) - self.altura + 40
        )
        self.qtd = 3

    def usar_penicilina(self):
        if(self.qtd > 0):
            self.set_qnt(self.qtd-1)
            return True
        return False

    def set_qnt(self, new_qnt):
        self.qtd = new_qnt

    def draw(self):
        self.janela.draw_text("x" + str(self.qtd), self.objeto.x + self.largura + 5,
                              self.objeto.y + self.altura - 35, size=35, color=(0, 0, 0))
        self.objeto.draw()
