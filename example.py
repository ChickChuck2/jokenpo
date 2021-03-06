import sys
from typing import Text
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui
import random
import time

# PyQt5 tem sua propia função de data e horas

#>Variaveis<#
default = 'style.css'

pedra = "Images/pedra.png"
papel = "Images/papel.png"
tesoura = "Images/tesoura.png"

block = "Images/block"

width = 800
height = 600

class Janela(QMainWindow):
    def __init__(self):
        super(Janela, self).__init__()

        #<!>Main<!>#
        #Titulo da janela
        self.setWindowTitle("Example")
        #Coloca um icone na janela
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        #tamanho da janela
        self.setGeometry(0,0,width,height)

        # <--- Text --->
        #cria o texto (QLabel é texto)
        self.texto1 = QLabel("Pedra papel ou tesourinha", self)
        #posição
        self.texto1.move(325,60)
        #redimencionamento
        self.texto1.resize(200,30)
        #alinhamento
        self.texto1.setAlignment(Qt.AlignLeft)
        # >--Fim do texto---<

        # <--- Button --->
        #cria o botão
        self.btnpedra = QPushButton("Pedra", self)
        #mover
        self.btnpedra.move(270,90)
        # se o botão for clicado (clicked) vai se conectar (connect) a uma (função)
        self.btnpedra.clicked.connect(self.funpedra)

        self.btnpapel = QPushButton("Papel", self)
        self.btnpapel.move(380,90)
        self.btnpapel.clicked.connect(self.funpapel)

        self.btntesoura = QPushButton("Tesoura", self)
        self.btntesoura.move(490,90)
        self.btntesoura.clicked.connect(self.funtesoura)


        self.maquina = QLabel("Maquina", self)
        self.maquina.move(90,160)
        self.maquina.resize(200,30)

        self.imageP1 = QLabel(self)
        self.pixp1 = QPixmap(block)
        self.imageP1.setPixmap(self.pixp1)
        self.imageP1.move(100,200)
        self.imageP1.resize(200,200)


        self.maquina = QLabel("Você", self)
        self.maquina.move(640,160)
        self.maquina.resize(200,30)

        self.imageP2 = QLabel(self)
        self.pixp2 = QPixmap(block)
        self.imageP2.setPixmap(self.pixp1)
        self.imageP2.move(500,200)
        self.imageP2.resize(200,200)
        self.show()

        # >>Style<<

        ##Button Confirm##
        self.btnpedra.setStyleSheet(open(default).read())
        self.btnpapel.setStyleSheet(open(default).read())
        self.btntesoura.setStyleSheet(open(default).read())

        #!!!!!Quando quiser adicionar um style, coloque aqui em cima
        
        #!!Important!!
        self.show()
    
    #!@ Funções @!
    def click(self):

        maquinanumero = ["0", "1", "2"]
        escolhaar = random.choice(maquinanumero)

        if escolhaar == "0":
            self.machinfuntesoura()
        if escolhaar == "1":
            self.machinfunpedra()
        if escolhaar == "2":
            self.machinfunpapel()
        
        playernum = ["0", "1", "2"]
        playchoce = random.choice(playernum)

        if playchoce == "0":
            self.funtesoura()
        if playchoce == "1":
            self.funpedra()
        if playchoce == "2":
            self.funpapel()

    def machinfuntesoura(self):
        self.imageP1.setPixmap(QPixmap(tesoura))

    def machinfunpedra(self):
        self.imageP1.setPixmap(QPixmap(pedra))

    def machinfunpapel(self):
        self.imageP1.setPixmap(QPixmap(papel))


    def funtesoura(self):
        self.imageP2.setPixmap(QPixmap(tesoura))
    def funpedra(self):
        self.imageP2.setPixmap(QPixmap(pedra))
    def funpapel(self):
        self.imageP2.setPixmap(QPixmap(papel))


# cor da janela em (CSS)
df = """
    Janela {
        background-color: green;
    }
"""

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # aqui você coloca o estilo da janela
    app.setStyleSheet(df)

    #define a janela
    janela = Janela()

    #mostra a janela
    janela.show()

    #Função para quando apertar no X pra sair
    sys.exit(app.exec_())