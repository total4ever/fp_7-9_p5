class Attending():
    def __init__(self, person, event):
        self.__person = person
        self.__event = event

    def getPersonID(self):
        return self.__person

    def getEventID(self):
        return self.__event

    def __eq__(self, other):
        return self.getPersonID() == other.getPersonID() and self.getEventID() == other.getEventID()