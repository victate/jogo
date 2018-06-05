from PPlay.gameimage import GameImage
from set_up import Popup_Images


class Popup:

    def __init__(self, janela):
        self.janela = janela

        self.objeto = GameImage(Popup_Images.inventario['fundo'])


    # popup(1) -> inventário
    # popup(2) -> prontuario
    def set_popup(self, tipo, soldado):

        self.tipo = tipo

        if (self.tipo == 1):
            self.texto = None
            self.objeto = GameImage(Popup_Images.inventario['fundo'])

            self.largura = self.objeto.width
            self.altura = self.objeto.height
            self.objeto.set_position(
                (self.janela.width / 2 - self.largura / 2),
                self.janela.height / 2 - self.altura / 2)

            self.bt_repor = Botao(self, self.janela, Popup_Images.inventario['bt_repor'], 2, 0, 0, 10)
            self.bt_dormir = Botao(self, self.janela, Popup_Images.inventario['bt_dormir'], 3, 1, 0, 10)
            self.bt_comer = Botao(self, self.janela, Popup_Images.inventario['bt_comer'], 4, 2, 0, 10)
            self.bt_ok = None
            self.bt_cancelar = None

        if (self.tipo == 2):
            self.texto = str(soldado.prontuario)
            self.objeto = GameImage(Popup_Images.prontuario['fundo'])

            self.largura = self.objeto.width
            self.altura = self.objeto.height
            self.objeto.set_position(
                (self.janela.width / 2 - self.largura / 2),
                self.janela.height / 2 - self.altura / 2)

            self.bt_ok = Botao(self, self.janela, Popup_Images.prontuario['bt_ok'], 13, 0, 0.5, 0)
            self.bt_cancelar = Botao(self, self.janela, Popup_Images.prontuario['bt_cancelar'], 14, 1, 0.5, 0)
            self.bt_repor = None
            self.bt_dormir = None
            self.bt_comer = None

        if (self.tipo == 0):
            self.texto = ""
            self.objeto = GameImage(Popup_Images.start['fundo'])
            self.largura = self.objeto.width
            self.altura = self.objeto.height
            self.objeto.set_position(
                (self.janela.width / 2 - self.largura / 2),
                self.janela.height / 2 - self.altura / 2)
            self.bt_ok = Botao(self, self.janela, Popup_Images.prontuario['bt_ok'], 10, 0, 0.7, 0)
            self.bt_cancelar = Botao(self, self.janela, Popup_Images.prontuario['bt_cancelar'], 13, 0, 0.7, 0)

            self.bt_repor = None
            self.bt_dormir = None
            self.bt_comer = None

    def draw(self):
        self.objeto.draw()

        self.janela.draw_text(self.texto, self.janela.width / 2 - self.largura / 2 + self.texto.__sizeof__()*2,
                              self.janela.height / 2 - self.altura / 4 + 40, size=20, color=(0, 0, 0), bold=True)
        if(self.tipo==1):
            self.bt_repor.draw()
            self.bt_dormir.draw()
            self.bt_comer.draw()
        elif(self.tipo==2 or self.tipo==0):
            self.bt_cancelar.draw()
            self.bt_ok.draw()


    def bt_clicked(self):
        mouse = self.janela.get_mouse()
        if (self.tipo == 1):
            if self.bt_comer.is_clicked(mouse):
                return 3
            if self.bt_dormir.is_clicked(mouse):
                return 2
            if self.bt_repor.is_clicked(mouse):
                return 1


        elif (self.tipo == 2 or self.tipo == 0):
            if self.bt_cancelar.is_clicked(mouse):
                return 0
            if self.bt_ok.is_clicked(mouse):
                return 4
        return 0

class Botao:

    def __init__(self, popup, janela, nome_image, mult_y, add_y, mult_x, add_x):
        self.janela = janela
        self.popup = popup
        self.objeto = GameImage(nome_image)
        self.largura = self.objeto.width
        self.altura = self.objeto.height
        self.x = self.janela.width/2 - popup.largura / 2 + mult_x*self.largura+add_x
        self.y = self.janela.height/2 - popup.altura/2 + mult_y*self.altura + add_y
        self.objeto.set_position(self.x, self.y)

    def draw(self):
        self.objeto.draw()

    def is_clicked(self, mouse):
        mouse_p = mouse.get_position()
        if (self.x <= mouse_p[0] <= self.x + self.largura
                and self.y + self.altura >= mouse_p[1] >= self.y
                and mouse.is_button_pressed(1)):
            return True
