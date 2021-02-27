import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui
import random

Lista = ["Lista", "baka", "relogio", "Vidro"]

# PyQt5 tem sua propia função de data e horas

#>Variaveis<#
default = 'style.css'

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

        escolha = random.choice(Lista)

        # <--- Text --->
        #cria o texto (QLabel é texto)
        self.texto1 = QLabel("MENSAGEM", self)
        #posição
        self.texto1.move(390,460)
        #redimencionamento
        self.texto1.resize(200,30)
        #alinhamento
        self.texto1.setAlignment(Qt.AlignLeft)
        # >--Fim do texto---<
        
        # <--- Image --->
        #cria uma area para a imagem ficar
        image = QLabel(self)
        # Cria a imagem
        pixmap = QPixmap('image.png')
        #seleciona a imagem
        image.setPixmap(pixmap)
        #move ela
        image.move(0,0)
        #redimenciona
        image.resize(120,140)
        # >--- Fim da imagem ---<
        ###
        ###
        
        # <--- Button --->
        #cria o botão
        self.botao = QPushButton("button", self)
        #mover
        self.botao.move(650,550)
        # se o botão for clicado (clicked) vai se conectar (connect) a uma (função)
        self.botao.clicked.connect(self.click)
        # >--- Fim da area do Button ---<
        
        # <--- TextBox --->
        #cria uma area para escrever
        self.textbox = QLineEdit(self)
        #mover
        self.textbox.move(390,500)
        #redimencionar
        self.textbox.resize(200,40) 

        # >>Style<<

        ##Button Confirm##
        self.botao.setStyleSheet(open(default).read())

        #!!!!!Quando quiser adicionar um style, coloque aqui em cima
        
        #!!Important!!
        self.show()

    #!@ Funções @!

    def click(self):
        escolha = random.choice(Lista)
        
        # mudar texto (QLabel)
        self.texto1.setText(escolha)

        #mudar titulo
        self.setWindowTitle(escolha)
        #
        print("adasd")

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