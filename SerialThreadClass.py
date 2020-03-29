import serial,serial.tools.list_ports
from PyQt5.QtCore import pyqtSignal, QThread

ports = [
    p.device
    for p in serial.tools.list_ports.comports()
    if 'USB' in p.description
]

if not ports:
    raise IOError("No devices found")

class SerialThreadClass(QThread):
    message = pyqtSignal(str)
    
    def __init__(self,parent=None):
        super(SerialThreadClass,self).__init__(parent)
        self.serialport = serial.Serial()
        self.serialport.baudrate = 9600
        if ports:
            self.serialport.port = ports[0]
            self.serialport.open()
    
    def run(self):
        while True:
            msg = self.serialport.readline()
            self.message.emit(str(msg))
            print(msg)
    
    def sendSerial(self,message):
        self.serialport.write(message)

    def setBaudRate(self,baudrate):
        self.serialport.baudrate = baudrate 
    
    def setSerialPort(self,port):
        self.serialport.port = port 