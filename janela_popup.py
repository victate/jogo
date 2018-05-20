from PPlay.gameimage import GameImage

class Popup:

    def __init__(self, janela):
        self.janela = janela
        self.objeto = GameImage("images/popup_inventario.png")
        self.largura = self.objeto.width
        self.altura = self.objeto.height
        self.objeto.set_position(
            (self.janela.width/2 - self.largura/2),
            self.janela.height/2 - self.altura/2)

        self.bt_repor = botao(self, self.janela, "images/botao_repor_inventario.png", 2, 0)
        self.bt_dormir = botao(self, self.janela, "images/botao_dormir.png", 3, 1)
        self.bt_comer = botao(self, self.janela, "images/botao_comer.png", 4, 2)

    def draw(self):
        self.objeto.draw()
        self.bt_repor.draw()
        self.bt_dormir.draw()
        self.bt_comer.draw()

    def bt_clicked(self):
        mouse = self.janela.get_mouse()

        if self.bt_comer.is_clicked(mouse):
            return 3
        if self.bt_dormir.is_clicked(mouse):
            return 2
        if self.bt_repor.is_clicked(mouse):
            return 1

        return 0

class botao():
    def __init__(self, popup, janela, nome_image, mult_y, add_y):
        self.janela = janela
        self.popup = popup
        self.objeto = GameImage(nome_image)
        self.largura = self.objeto.width
        self.altura = self.objeto.height
        self.x = self.janela.width/2 - popup.largura / 2 + 10
        self.y = self.janela.height/2 - popup.altura/2 + mult_y*self.altura + add_y
        self.objeto.set_position(self.x, self.y)

    def draw(self):
        self.objeto.draw()

    def is_clicked(self, mouse):
        mouse_p = mouse.get_position()
        if (mouse_p[0] >= self.x and mouse_p[0] <= self.x + self.largura
                and mouse_p[1] <= self.y + self.altura and mouse_p[1] >= self.y
                and mouse.is_button_pressed(1)):
            return True