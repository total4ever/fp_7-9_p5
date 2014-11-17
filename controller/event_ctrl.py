from domain.event import Event
class EventCtrl():
    def __init__(self, validator, repo):
        self.__validator = validator
        self.__repo = repo

    def addEvent(self, eventID, date, time, desc):
        event = Event(eventID, date, time, desc)

        self.__validator.validate_event(event)
        self.__repo.add(event)

    def getAll(self):
        return self.__repo.findAll()