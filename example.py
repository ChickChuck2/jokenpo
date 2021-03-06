import sys
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
        self.btnpedra = QPushButton("Pedra", self)#cria o botão
        self.btnpedra.move(270,90)#mover
        self.btnpedra.clicked.connect(self.funpedra)# se o botão for clicado vai se conectar a uma (função)

        self.btnpapel = QPushButton("Papel", self)
        self.btnpapel.move(380,90)
        self.btnpapel.clicked.connect(self.funpapel)
        self.btnpapel.clicked.connect(self.papel)

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

        #Maquina Stats
        self.pontos = QLabel("Pontos: ",self)
        self.pontos.move(100, 400)
        self.pontos.resize(100,30)

        self.ganhos = QLabel("Ganhos: ",self)
        self.ganhos.move(100, 410)
        self.ganhos.resize(100,30)

        self.winconsecs = QLabel("Ganhos Consecutivos: ",self)
        self.winconsecs.move(100, 420)
        self.winconsecs.resize(105,30)

        self.empate = QLabel("Empates: ",self)
        self.empate.move(100, 430)
        self.empate.resize(100,30)

        #Player Stats
        self.P1pontos = QLabel("Pontos: ",self)
        self.P1pontos.move(500, 400)
        self.P1pontos.resize(100,30)

        self.P1ganhos = QLabel("Ganhos: ",self)
        self.P1ganhos.move(500, 410)
        self.P1ganhos.resize(100,30)

        self.P1winconsecs = QLabel("Ganhos Consecutivos: ",self)
        self.P1winconsecs.move(500, 420)
        self.P1winconsecs.resize(105,30)

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

    def machinfuntesoura(self):
        self.imageP1.setPixmap(QPixmap(tesoura))

    def machinfunpedra(self):
        self.imageP1.setPixmap(QPixmap(pedra))

    def machinfunpapel(self):
        self.imageP1.setPixmap(QPixmap(papel))
        self.machinpapel()


    def funtesoura(self):
        self.imageP2.setPixmap(QPixmap(tesoura))

        maquinanumero = ["0", "1", "2"]
        escolhaar = random.choice(maquinanumero)

        if escolhaar == "0":
            self.machinfuntesoura()
        if escolhaar == "1":
            self.machinfunpedra()
        if escolhaar == "2":
            self.machinfunpapel()

    def funpedra(self):
        self.imageP2.setPixmap(QPixmap(pedra))

        maquinanumero = ["0", "1", "2"]
        escolhaar = random.choice(maquinanumero)

        if escolhaar == "0":
            self.machinfuntesoura()
        if escolhaar == "1":
            self.machinfunpedra()
        if escolhaar == "2":
            self.machinfunpapel()

    def funpapel(self):
        self.imageP2.setPixmap(QPixmap(papel))

        maquinanumero = ["0", "1", "2"]
        escolhaar = random.choice(maquinanumero)

        if escolhaar == "0":
            self.machinfuntesoura()
        if escolhaar == "1":
            self.machinfunpedra()
        if escolhaar == "2":
            self.machinfunpapel()

    def papel(self):
        self.twa = print("Papel entrou")
    
    def machinpapel(self):
        self.v = print("Papel MAQUINA entrou")
    
    def empate(self):

        if self.machinpapel + self.papel:
            print("EMPATE")
                 

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