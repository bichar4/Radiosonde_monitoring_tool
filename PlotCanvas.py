import sys 

from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random 
class PlotCanvas(FigureCanvas):
    def __init__(self,parent = None, width=5, height = 9, dpi = 100):
        self.data = []
        self.fig = Figure(figsize=(width,height), dpi= dpi)
        self.axes = self.fig.add_subplot(111)

        FigureCanvas.__init__(self,self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,QSizePolicy.Expanding,QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()
        

    def plot(self):
        self.axes.clear()
        self.axes.plot(self.data)#for printing the recent 100 data only 
        self.draw()
        #print(self.axes.lines)
        
    def updatePlot(self,count):      
        self.data.append(count)
        self.data = self.data[-100:]
        #print(self.axes.lines)
        self.plot()

