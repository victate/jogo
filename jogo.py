from PPlay.window import *

import Enfermeira
import Soldado
from Cirurgia import *
from Hud import *
from janela_popup import *

fundo_largura = 708
fundo_altura = 708


janela = Window(fundo_largura, fundo_altura)
fundo = GameImage("images/fundo.jpg")
janela_largura = fundo.width
janela_altura = fundo.height

# Teclado
teclado = janela.get_keyboard()

# Mouse
mouse = janela.get_mouse()

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

inicio_espaco = cirurgia.objeto.y + cirurgia.altura - ((3 * enfermeira.altura) / 4) + enfermeira.altura
fim_espaco = hud.objeto.y + (2 * enfermeira.altura / 5)

espacos_entre_camas = Soldado.espacos_entre_camas(soldados, inicio_espaco, fim_espaco)
espacos_camas = Soldado.espacos_camas(espacos_entre_camas)

# Popup
popup = Popup(janela)
abrir_popup = False

#ciclo
time = 100
ciclo = 0.5*1000*60

while True:

    fundo.draw()
    cirurgia.draw()
    if not abrir_popup:
        enfermeira.mover(enfermeira_direita, enfermeira_esquerda, soldados,
                         teclado, inicio_espaco, fim_espaco, espacos_entre_camas, espacos_camas)
    hud.draw()
    penicilina.draw()
    bandagem.draw()
    barras.draw()

    if(janela.time_elapsed() - time >= ciclo):
        abrir_popup = True

    if abrir_popup:
        popup.draw()
        acao = popup.bt_clicked()
        if acao > 0:
            #if acao==3:
                # repoe barra comida
            #if acao==2:
                # repoe sono
            if acao == 1:
                penicilina.set_qnt(3)
                bandagem.set_qnt(3)
            abrir_popup = False
        time = janela.time_elapsed()

    for soldado in soldados:
        if(enfermeira.colisao(soldado)):
            print(soldado.prontuario)

    janela.update()
