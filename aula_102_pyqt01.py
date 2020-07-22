# Primeira aula PyQt5

# PyQT é um toolkit desenvolvido em C++ utilizado por vários programas para
# criação de aplicações GUI (Interface Gráfica). Também  inclui diversas
# funcionalidades, como: acesso a base de dados, threads, comunicação de rede,
# etc

# pip install pyqt5

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, \
    QGridLayout, QLabel, QTextEdit


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.clicado = False
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.lbl = QLabel('Texto qualquer')
        self.txt1 = QTextEdit('Oi')
        self.btn = QPushButton('Texto do botão')

        self.grid.addWidget(self.btn, 0, 0, 1, 1)
        self.grid.addWidget(self.lbl, 1, 0, 1, 1)
        self.grid.addWidget(self.txt1, 2, 0, 1, 1)

        self.btn.clicked.connect(self.acao)

        self.setCentralWidget(self.cw)

        # A customização igual as propriedades no CSS
        self.cw.setStyleSheet('background: white;')
        self.btn.setStyleSheet('font-size: 40px; color: blue;')
        self.lbl.setStyleSheet('font-size: 40px; color: red;')
        self.txt1.setStyleSheet('font-size: 35px;')

    def acao(self):
        if not self.clicado:
            self.cw.setStyleSheet('background: white;')
            self.lbl.setText('Tudo')
        else:
            self.cw.setStyleSheet('background: gray;')
            self.lbl.setText('Bem?')
        self.clicado = not self.clicado


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
