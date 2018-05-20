from random import randint

prontuario = ["bandagem", "penicilina", "cirurgia"]

def gerar_prontuario():
    num_gerado = randint(0,2)
    return prontuario[num_gerado]