import sys 
import serial.tools.list_ports
from PyQt5.QtWidgets import QApplication,QDialog
from serialMonitor_ui import *
from SerialThreadClass import *
from Packet_Tokenizer import *

ports = [
    p.device
    for p in serial.tools.list_ports.comports()
    if 'USB' in p.description
]


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
        self.show()

    def intrepret_packet(self,packet):
        self.ui_Serial.SerialOutput.append(packet)
        self.parser.extractData(packet)
        print(self.parser.getData())
        

    def btnClickedEvent(self):
        self.myserial.sendSerial()
        print('Pressing') 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainClass()
    sys.exit(app.exec_())