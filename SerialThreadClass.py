import serial
from PyQt5.QtCore import pyqtSignal, QThread


#if not ports:
#   raise IOError("No devices found")

class SerialThreadClass(QThread):
    message = pyqtSignal(str)
    
    def __init__(self,parent=None,port = '/dev/ttyUSB0', baudrate = 9600):
        super(SerialThreadClass,self).__init__(parent)
        self.serialport = serial.Serial()
        self.serialport.baudrate = baudrate
        self.serialport.port = port
        self.serialport.open()

    def run(self):
        while True:
            msg = self.serialport.readline()
            self.message.emit(msg.decode('utf-8'))
    
    def sendSerial(self,message):
        self.serialport.write(message)

    def setBaudRate(self,baudrate):
        self.serialport.baudrate = baudrate 
    
    def setSerialPort(self,port):
        self.serialport.port = port 