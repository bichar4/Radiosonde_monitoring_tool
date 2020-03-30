import sys 

from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import random 
class PlotCanvas(FigureCanvas):
    def __init__(self,parent = None, width=5, height = 9, dpi = 100):
        self.data = []
        fig = Figure(figsize=(width,height), dpi= dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self,fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,QSizePolicy.Expanding,QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()
        

    def plot(self):
        print("I am in")
        self.axes.plot(self.data)
        self.axes.set_title('Example plot')
        self.draw()
        print(self.axes.lines)
        
        

    def updatePlot(self,count):
        
        line = self.axes.lines[0]
        self.data.append(2*random.random())
        line.set_xdata(np.append(line.get_xdata(),count))
        line.set_ydata(self.data)
        print(self.axes.lines)
        self.plot()