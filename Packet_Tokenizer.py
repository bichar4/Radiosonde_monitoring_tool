class Packet_Tokenizer():
    def __init__(self):
        self.packet = {}
        self.number_of_keys = 0
    def assign_key(self,list_of_keys):
        """
        dynamic assign of keys given as list by client 
        """
        self.packet = dict.fromkeys(list_of_keys,None)
        self.number_of_keys = len(list_of_keys)

    def updateDictionary(self,dataList):
        assert len(self.packet) == len(dataList),"number of keys and recived number of fields donot match"  
        i = 0
        for k,v in self.packet.items():
            self.packet[k] = dataList[i]
            i+=1
    
    def getData(self):
        return self.packet
    
    def extractData(self,packet):
        """
            Extracts the data packet which is in form of string with delimiter comma and updates the 
            value of dictionaty
        """
        packet = packet.replace("\r\n","")
        dataList = packet.split(',')
        if dataList[0] == '$':
            self.updateDictionary(dataList[1:])
        else:
            pass
        
    def test(self):
        print(self.packet)