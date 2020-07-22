# Calculadora com PyQt5

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QSizePolicy


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora do Five')
        self.setFixedSize(400, 400)

        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.setStyleSheet('background: #446665;')

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            '*{'
            'background: #9db8cc;'
            'color: black;'
            'border: 1px solid black;'
            'font-size: 20px;'
            'border-radius: 5px;'
            '}')
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.add_btn(QPushButton('7'), 1, 0, 1, 1)
        self.add_btn(QPushButton('8'), 1, 1, 1, 1)
        self.add_btn(QPushButton('9'), 1, 2, 1, 1)
        self.add_btn(QPushButton('+'), 1, 3, 1, 1)
        self.add_btn(
            QPushButton('<-'),
            1, 4, 1, 1,
            funcao=lambda:
            self.display.setText(self.display.text()[:-1])
        )

        self.add_btn(QPushButton('6'), 2, 0, 1, 1)
        self.add_btn(QPushButton('5'), 2, 1, 1, 1)
        self.add_btn(QPushButton('4'), 2, 2, 1, 1)
        self.add_btn(QPushButton('-'), 2, 3, 1, 1)
        self.add_btn(
            QPushButton('='),
            2, 4, 3, 1,
            funcao=self.eval_igual
        )

        self.add_btn(QPushButton('3'), 3, 0, 1, 1)
        self.add_btn(QPushButton('2'), 3, 1, 1, 1)
        self.add_btn(QPushButton('1'), 3, 2, 1, 1)
        self.add_btn(QPushButton('*'), 3, 3, 1, 1)
        # self.add_btn(QPushButton('?'), 3, 4, 1, 1)

        self.add_btn(QPushButton('0'), 4, 0, 1, 1)
        self.add_btn(QPushButton('.'), 4, 1, 1, 1)
        self.add_btn(
            QPushButton('C'),
            4, 2, 1, 1,
            funcao=lambda: self.display.setText('')
        )
        self.add_btn(QPushButton('/'), 4, 3, 1, 1)
        # self.add_btn(QPushButton('?'), 4, 4, 1, 1)

        self.setCentralWidget(self.cw)

    def add_btn(self, btn, row, col, rowspan, colspan, funcao=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)
        if not funcao:
            btn.clicked.connect(
                lambda: self.display.setText(self.display.text() + btn.text())
            )
        else:
            btn.clicked.connect(funcao)
        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        btn.setStyleSheet(
            'font-size: 20px;'
            'color: #423a04;'
            'background: #ffb759;'
            'border-radius: 5px;'
        )

    def eval_igual(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )
        except Exception:
            self.display.setText('Conta inválida.')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()
