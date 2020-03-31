import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
import random

from PlotCanvas import *

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.title = 'PyQt5 matplotlib example - pythonspot.com'
        self.width = 640*2
        self.height = 400
        self.m = PlotCanvas(self, width=5, height=4)
        self.n = PlotCanvas(self,width=5,height = 4)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.updatePlot)
        timer.start(100)
        self.seconds = 0
        self.initUI()

    def updatePlot(self):
        self.seconds+=1
        self.m.updatePlot(self.seconds*self.seconds)
        self.n.updatePlot(5*self.seconds + 1)
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

      
        self.m.move(0,0)
        self.n.move(640,0)

        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This s an example button')
        button.move(500,0)
        button.resize(140,100)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())