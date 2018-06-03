import Enfermeira
import Soldado
from Cirurgia import *
from Hud import *
from PPlay.window import *
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
barra_fome = BarraFome(barras)
barra_sono = BarraSono(barras)

inicio_espaco = cirurgia.objeto.y + cirurgia.altura - ((3 * enfermeira.altura) / 4) + enfermeira.altura
fim_espaco = hud.objeto.y + (2 * enfermeira.altura / 5)

espacos_entre_camas = Soldado.espacos_entre_camas(soldados, inicio_espaco, fim_espaco)
espacos_camas = Soldado.espacos_camas(espacos_entre_camas)

# Popup
abrir_popup = False
popup = Popup(janela)

# ciclo
time = 100
ciclo = 0.1*1000*60


while True:
    fundo.draw()
    cirurgia.draw()
    tempo_atual = janela.time_elapsed()


    if not abrir_popup:
        enfermeira.mover(enfermeira_direita, enfermeira_esquerda, soldados,
                         teclado, inicio_espaco, fim_espaco, espacos_entre_camas, espacos_camas)

    if tempo_atual - time >= ciclo:
        for soldado in soldados:
            if not soldado.status:
                soldado.status = True
        popup.set_popup(1, None)
        abrir_popup = True

    if abrir_popup:
        popup.draw()
        acao = popup.bt_clicked()
        if acao > 0:
            if acao == 3:
                Barras.comer(barra_fome)
            elif acao == 2:
                Barras.dormir(barra_sono)
            elif acao == 1:
                Barras.repor_inventario(penicilina, bandagem)
            elif acao == 4:
                if soldado_ativo.prontuario == 'bandagem':
                    #soldado_ativo.prontuario está salvo
                    #numero de soldados em campo aumenta
                    bandagem.usar_bandagem()

                elif soldado_ativo.prontuario == 'penicilina':
                    # soldado_ativo.prontuario está salvo
                    # numero de soldados em campo aumenta
                    penicilina.usar_penicilina()

                elif soldado_ativo.prontuario == 'cirurgia':
                    soldado_ativo.status = False

            abrir_popup = False
        time = tempo_atual

    for soldado in soldados:
        if enfermeira.colisao(soldado):
            soldado_ativo = soldado
            popup.set_popup(2, soldado_ativo)
            abrir_popup = True

    # Diminui a barra de sono e de fome gradualmente
    barra_sono.aumenta_sono(tempo_atual)
    barra_fome.aumenta_fome(tempo_atual)

    # Desenha os objetos
    hud.draw()
    penicilina.draw()
    bandagem.draw()
    barras.draw()
    barra_fome.draw()
    barra_sono.draw()

    janela.update()
