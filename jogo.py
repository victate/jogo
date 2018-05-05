from PPlay.window import *

import Enfermeira
import Soldado
from Cirurgia import *
from Hud import *


fundo_largura = 708
fundo_altura = 708


janela = Window(fundo_largura, fundo_altura)
fundo = GameImage("images/fundo.jpg")
janela_largura = fundo.width
janela_altura = fundo.height

# Teclado
teclado = janela.get_keyboard()


# Enfermeira
enfermeira = Enfermeira.Enfermeira(janela)
enfermeira_direita = Enfermeira.EnfermeiraDireita(janela_largura, janela_altura)
enfermeira_esquerda = Enfermeira.EnfermeiraEsquerda(janela_largura, janela_altura)

# Cirurgia
cirurgia = Cirurgia(janela)


# Soldado
soldados = []
for i in range(150, 500, 85):
    soldados.append(Soldado.SoldadoEsquerda(janela, i))
    soldados.append(Soldado.SoldadoDireita(janela, i))

# Hud
hud = Hud(janela)

# Penicilina
penicilina = Penicilina(hud, janela)

# Bandagem
bandagem = Bandagem(hud, janela)

# Barras
barras = Barras(hud)


while True:
    fundo.draw()
    cirurgia.draw()

    enfermeira.mover(enfermeira_direita, enfermeira_esquerda, soldados, teclado, 111, 495)

    hud.draw()
    penicilina.draw()
    bandagem.draw()
    barras.draw()
    janela.update()
