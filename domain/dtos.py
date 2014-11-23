class AttentingDTO():
    def __init__(self, eventID, personID):
        self.__eventID = eventID
        self.__personID = personID

        self.__personName = ""

        self.__eventDate = ""
        self.__eventDesc = ""

        self.__personEvents = 0
        self.__eventPersons = 0


    def getEventID(self):
        return self.__eventID

    def getPersonID(self):
        return self.__personID

    def getEventDate(self):
        return self.__eventDate

    def getEventDesc(self):
        return self.__eventDesc

    def getPersonEvents(self):
        return self.__personEvents

    def getEventPersons(self):
        return self.__eventPersons

    def getPersonName(self):
        return self.__personName

    def setPersonName(self, name):
        self.__personName = name

    def setEventDate(self, data):
        self.__eventDate = data

    def setEventDesc(self, data):
        self.__eventDesc = data

    def incEvents(self):
        self.__personEvents += 1

    def incPersons(self):
        self.__eventPersons += 1
