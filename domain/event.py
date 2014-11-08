class Event():
    def __init__(self, ID, date, time, desc):
        self.__ID = ID
        self.__date = date
        self.__time = time
        self.__desc = desc
    
    def setDate(self, date):
        self.__date = date
    
    def setTime(self, time):
        self.__time = time
    
    def setDesc(self, desc):
        self.__desc = desc
    
    def getID(self):
        return self.__ID
    
    def getDate(self):
        return self.__date
    
    def getTime(self):
        return self.__time
    
    def getDesc(self):
        return self.__desc

    def __eq__(self, ot):
        return self.__ID == ot.__ID and self.__date == ot.__date and self.__time == ot.__time and self.__desc == ot.__desc
    