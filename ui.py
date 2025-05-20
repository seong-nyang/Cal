from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QPlainTextEdit, QHBoxLayout)

from PyQt5.QtGui import QIcon

class View (QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.tel = QPlainTextEdit()
        self.tel.setReadOnly(True)

        self.btn1=QPushButton('Message', self)
        self.btn2=QPushButton('Clear', self)

        hbox = QHBoxLayout()
        hbox.addStretch (1)
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)
    
        vbox=QVBoxLayout()
        vbox.addWidget(self.tel)
        vbox.addLayout(hbox)
        vbox.addStretch (1)

        self.setLayout(vbox)
        
        self.setWindowTitle('Calculator')
        self.setWindowIcon (QIcon('icon.png'))
        self.resize(256,256)
        self.show()

    def activateMessage(self):
        self.tel.appendPlainText("Button clicked!")
    def clearMessage(self): self.tel.clear()