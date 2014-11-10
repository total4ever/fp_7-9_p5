class Person():
    def __init__(self, personID, name, addr):
        self.__personID = personID
        self.__name = name
        self.__addr = addr
        
    def setName(self, name):
        self.__name = name
    
    def setAddr(self, addr):
        self._addr = addr
        
    def getID(self):
        return self.__personID
    
    def getName(self):
        return self.__name
    
    def getAddr(self):
        return self.__addr

    def __eq__(self, ot):
        return self.__personID == ot.__personID