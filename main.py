import sys,traceback 
import serial.tools.list_ports
from PyQt5.QtWidgets import QApplication,QDialog
from serialMonitor_ui import *
from SerialThreadClass import *
from Packet_Tokenizer import *
import random
from PlotCanvas import * 

from PyQt5.QtCore import *

ports = [
    p.device
    for p in serial.tools.list_ports.comports()
    if 'USB' in p.description
]

class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data
    
    error
        `tuple` (exctype, value, traceback.format_exc() )
    
    result
        `object` data returned from processing, anything

    progress
        `int` indicating % progress 

    '''
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and 
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()    

       

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        
        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done
        

class MainClass(QDialog):
    def __init__(self):
        super().__init__()
        self.ui_Serial = Ui_Serial()
        self.ui_Serial.setupUi(self)
        self.ui_Serial.SendButton.clicked.connect(self.btnClickedEvent)
        self.myserial = SerialThreadClass(port = ports[0])
        self.myserial.message.connect(self.intrepret_packet)
        self.myserial.start()
        self.parser = Packet_Tokenizer()
        self.parser.assign_key(['nodeId','temp','humidity','pressure','latitude','longitude'])
        
        self.m = PlotCanvas(self, width=5, height=4)
        self.m.move(500,0)
         
        self.n = PlotCanvas(self, width=5, height=4)
        self.n.move(500,450)

          
        self.o = PlotCanvas(self, width=5, height=4)
        self.o.move(0,650)

        self.threadpool = QThreadPool()
        self.show()

    def intrepret_packet(self,packet):
        self.ui_Serial.SerialOutput.append(packet)
        self.parser.extractData(packet)
        value = self.parser.getData()['nodeId']
        if value is not None:
            worker1 = Worker(self.m.updatePlot,int(value)+random.randint(1,10))
            worker2 = Worker(self.n.updatePlot,int(value))
            worker3 = Worker(self.o.updatePlot,3)
            # self.n.updatePlot(int(value)+random.randint(1,10))
            # self.o.updatePlot(int(value)+random.randint(1,10))
            self.threadpool.start(worker1)
            self.threadpool.start(worker2)
            self.threadpool.start(worker3) 

    def btnClickedEvent(self):
        self.myserial.sendSerial(b'test')
        print('Pressing') 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainClass()
    sys.exit(app.exec_())