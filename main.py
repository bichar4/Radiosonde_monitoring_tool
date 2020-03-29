import sys 
from PyQt5.QtWidgets import QApplication,QDialog
from serialMonitor_ui import *
from SerialThreadClass import *
class MainClass(QDialog):
    def __init__(self):
        super().__init__()
        self.ui_Serial = Ui_Serial()
        self.ui_Serial.setupUi(self)
        self.ui_Serial.SendButton.clicked.connect(self.btnClickedEvent)
        self.myserial = SerialThreadClass()
        self.myserial.message.connect(self.ui_Serial.SerialOutput.append)
        self.myserial.start()

        self.show()

    def btnClickedEvent(self):
        self.myserial.sendSerial()
        print('Pressing') 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainClass()
    sys.exit(app.exec_())