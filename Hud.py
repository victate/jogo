from PPlay.gameimage import *


class Hud:

    def __init__(self, janela):
        self.janela = janela

        self.objeto = GameImage("images/hud_status.png")

        self.largura = self.objeto.width
        self.altura = self.objeto.height
        self.objeto.set_position(
            (self.janela.width - self.largura) / 2,
            self.janela.height - self.altura - 10
        )
        self.status = 99
        self.status2 = 99

    def draw(self):
        self.objeto.draw()
        self.janela.draw_text(str(self.status), self.objeto.x + self.largura - 120,
                              self.objeto.y + self.altura - 70, size=44, color=(0, 0, 0), bold=True)
        self.janela.draw_text("/" + str(self.status2), self.objeto.x + self.largura - 73,
                              self.objeto.y + self.altura - 64, size=35, color=(255, 0, 0), bold=True)


class Bandagem:

    def __init__(self, hud, janela):
        self.janela = janela
        self.hud = hud

        self.objeto = GameImage("images/bandagem.png")
        self.largura = self.objeto.width
        self.altura = self.objeto.height
        self.objeto.set_position(
            (self.hud.largura / 5) + (self.largura / 2) + 10,
            self.hud.objeto.y + (self.hud.altura / 2) - self.altura + 40
        )
        self.qtd = 99

    def draw(self):
        self.janela.draw_text("x" + str(self.qtd), self.objeto.x + self.largura + 5,
                              self.objeto.y + self.altura - 35, size=35, color=(0, 0, 0))
        self.objeto.draw()


class Barras:

    def __init__(self, hud):
        self.hud = hud
        self.objeto = GameImage("images/barras.png")
        self.largura = self.objeto.width
        self.altura = self.objeto.height
        self.objeto.set_position(
            (self.hud.largura / 2) - (self.largura / 2) + 75,
            self.hud.objeto.y + (self.hud.altura / 2) - (self.altura / 2)
        )

    def draw(self):
        self.objeto.draw()


class Penicilina:

    def __init__(self, hud, janela):
        self.hud = hud
        self.janela = janela

        self.objeto = GameImage("images/penicilina.png")
        self.largura = self.objeto.width
        self.altura = self.objeto.height
        self.objeto.set_position(
            (self.hud.largura / 40) + (self.largura / 2),
            self.hud.objeto.y + (self.hud.altura / 2) - self.altura + 40
        )
        self.qtd = 99

    def draw(self):
        self.janela.draw_text("x" + str(self.qtd), self.objeto.x + self.largura + 5,
                              self.objeto.y + self.altura - 35, size=35, color=(0, 0, 0))
        self.objeto.draw()
