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

        self.empates = 0

        self.pontosM1 = 0

        self.pontosP1 = 0

        #<!>Main<!>#
        #Titulo da janela
        self.setWindowTitle("Example")
        #Coloca um icone na janela
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        #tamanho da janela
        self.setGeometry(0,0,width,height)

        # <--- Text --->
        
        self.texto1 = QLabel("Pedra papel ou tesourinha", self)#cria o texto (QLabel é texto)
        self.texto1.move(325,60)#posição
        self.texto1.resize(200,30)#redimencionamento
        self.texto1.setAlignment(Qt.AlignLeft)#alinhamento
        # >--Fim do texto---<

        # <--- Button --->
        
        self.btnpedra = QPushButton("Pedra", self)#cria o botão
        self.btnpedra.move(270,90)#mover
        self.btnpedra.clicked.connect(self.funpedra)# se o botão for clicado vai se conectar a uma (função)

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


        #MAQUINA 
        self.pontos1 = QLabel(f"Pontos: {self.pontosM1}", self)
        self.pontos1.move(90,400)
        self.pontos1.resize(200,30)

        self.ganhos1 = QLabel(f"Ganhos: ", self)
        self.ganhos1.move(90,410)
        self.ganhos1.resize(200,30)

        self.ganhoscons1 = QLabel(f"Ganhos consecutivos: ", self)
        self.ganhoscons1.move(90,420)
        self.ganhoscons1.resize(200,30)

        self.empate = QLabel(f"Empate: {self.empates}", self)
        self.empate.move(350,430)
        self.empate.resize(200,30)

        #Player SYSTEM
        self.pontos2 = QLabel(f"Pontos: {self.pontosP1}", self)
        self.pontos2.move(500,400)
        self.pontos2.resize(200,30)

        self.ganhos2 = QLabel(f"Ganhos: ", self)
        self.ganhos2.move(500,410)
        self.ganhos2.resize(200,30)

        self.ganhoscons2 = QLabel(f"Ganhos consecutivos: ", self)
        self.ganhoscons2.move(500,420)
        self.ganhoscons2.resize(200,30)

        # >>Style<<

        ##Button Confirm##
        self.btnpedra.setStyleSheet(open(default).read())
        self.btnpapel.setStyleSheet(open(default).read())
        self.btntesoura.setStyleSheet(open(default).read())

        #!!!!!Quando quiser adicionar um style, coloque aqui em cima
        
        #!!Important!!
        self.show()
    
    #!@ Funções @!

    #escolher maquina tesoura
    def machinfuntesoura(self):
        self.imageP1.setPixmap(QPixmap(tesoura))
    
    #escolher maquina pedra
    def machinfunpedra(self):
        self.imageP1.setPixmap(QPixmap(pedra))

    #escolher maquina papel
    def machinfunpapel(self):
        self.imageP1.setPixmap(QPixmap(papel))
        

    #player tesoura
    def funtesoura(self):
        self.imageP2.setPixmap(QPixmap(tesoura))

        maquinanumero = ["0", "1", "2"]
        escolhaar = random.choice(maquinanumero)

        if escolhaar == "0":
            self.machinfuntesoura()
            self.empatetesoura()

        if escolhaar == "1":
            self.machinfunpedra()
            self.pontomachipedra()

        if escolhaar == "2":
            self.machinfunpapel()

    #player pedra
    def funpedra(self):

        self.imageP2.setPixmap(QPixmap(pedra))

        maquinanumero = ["0", "1", "2"]
        escolhaar = random.choice(maquinanumero)

        if escolhaar == "0":
            self.machinfuntesoura()

        if escolhaar == "1":
            self.machinfunpedra()
            self.empatepedra()

        if escolhaar == "2":
            self.machinfunpapel()
            self.pontomachipapel()

    #player papel
    def funpapel(self):

        #comando para setar a imagem de papel do player
        self.imageP2.setPixmap(QPixmap(papel))

        maquinanumero = ["0", "1", "2"]
        escolhaar = random.choice(maquinanumero)

        #escolher maquina tesoura
        if escolhaar == "0":
            self.machinfuntesoura()
            self.pontomachitesoura()

        #escolher maquina pedra
        if escolhaar == "1":
            self.machinfunpedra()

        #escolher maquina papel
        if escolhaar == "2":
            self.machinfunpapel()
            self.empatepapel()
    
    #SISTEMA DE EMPATE
    def empatepapel(self):
        print("empate PAPEL")

        self.empates = self.empates + 1
        self.empate.setText(f"Empates: {self.empates}")
    
    def empatepedra(self):
        print("empate PEDRA")
        self.empates = self.empates + 1
        self.empate.setText(f"Empates: {self.empates}")
    
    def empatetesoura(self):
        print("EMPATE TESOURA")
        self.empates = self.empates + 1
        self.empate.setText(f"Empates: {self.empates}")
    #    FIM SISTEMA EMPATE

    #SISTMA DE PONTOS MAQUINA
    def pontomachipapel(self):
        self.pontosM1 = self.pontosM1 + 1
        print("Pontos papel")
        self.pontos1.setText(f"Pontos: {self.pontosM1}")
    
    def pontomachitesoura(self):
        print("pontos tesoura")
        self.pontosM1 = self.pontosM1 + 1
        self.pontos1.setText(f"Pontos: {self.pontosM1}")
    
    def pontomachipedra(self):
        self.pontosM1 = self.pontosM1 + 1
        print("pontos pedra")
        self.pontos1.setText(f"Pontos: {self.pontosM1}")

    #SISTEMA DE PONTOS PLAYER
    def pontopapel(self):
        self.pontosP1 = self.pontosP1 + 1
        self.pontos2.setText(f"Pontos: {self.pontosP1}")
        print("PONTO PAPEL")
    
    def pontopedra(self):
        print("PONTO PEDRA")
        self.pontosP1 = self.pontosP1 + 1
        self.pontos2.setText(f"Pontos: {self.pontosP1}")
    
    def pontotesoura(self):
        print("PONTO TESOURA")
        self.pontosP1 = self.pontosP1 + 1
        self.pontos2.setText(f"Pontos: {self.pontosP1}")
    

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