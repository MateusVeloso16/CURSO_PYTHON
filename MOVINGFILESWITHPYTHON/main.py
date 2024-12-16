import os

caminho = r"C:\Users\Precision5540\Desktop\Codigos\CURSO_PYTHON\MOVINGFILESWITHPYTHON"
lista_arquivos = os.listdir(caminho + r"\Mover")

for arquivo in lista_arquivos:
    if ".xlsx" in arquivo:
        if "Jan" in arquivo:
            #jogar para a pasta de janeiro
            os.rename(f"{caminho + r"\Mover"}/{arquivo}", f"{caminho + r"\Mover"}/Jan/{arquivo}")
        if "Fev" in arquivo:
            #jogar para a pasta de Fevereiro
            os.rename(f"{caminho + r"\Mover"}/{arquivo}", f"{caminho + r"\Mover"}/Fev/{arquivo}")
        if "Mar" in arquivo:
            #jogar para a pasta de marco
            os.rename(f"{caminho + r"\Mover"}/{arquivo}", f"{caminho + r"\Mover"}/Mar/{arquivo}")