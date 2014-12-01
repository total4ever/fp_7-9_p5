from domain.attending import Attending
from domain.dtos import AttentingDTO


class AttentingCtrl():
    def __init__(self, val, eventRepo, personRepo, attendingRepo):
        self.__val = val
        self.__eventRepo = eventRepo
        self.__personRepo = personRepo
        self.__attentingRepo = attendingRepo


    def attend(self, personID, eventID):
        #person = self.__personRepo.find(personID)
        #event = self.__eventRepo.find(eventID)

        attending = Attending(personID, eventID)

        self.__val.validate_attenting(attending)

        self.__attentingRepo.add(attending)


    def personEvents(self, personID):
        all = self.__attentingRepo.getAll()

        final = []
        for atd in all:
            if personID == atd.getPersonID():
                final.append(atd)

        for i in range(len(final)):
            x = self.__eventRepo.find(final[i].getEventID())

            final[i].setEventDesc(x.getDesc())
            final[i].setEventDate(x.getDate())

        #return final
        return sorted(final, key=lambda e: e.getEventDesc())

    def personsWithMostEvents(self):
        all = self.__attentingRepo.getAll()

        final = []

        for atd in all:
            curr = -1

            for i in range(len(final)):
                if final[i].getPersonID() == atd.getPersonID():
                    curr = i

            if curr != -1:
                final[curr].incEvents()
            else:
                x = AttentingDTO(atd.getEventID(), atd.getPersonID())
                x.incEvents()
                final.append(x)

        for i in range(len(final)):
            x = self.__personRepo.find(final[i].getPersonID())

            final[i].setPersonName(x.getName())
        return sorted(final, key=lambda e: e.getPersonEvents(), reverse=True)

    def eventsWithMostPersons(self):
        all = self.__attentingRepo.getAll()

        final = []

        for atd in all:
            curr = -1

            for i in range(len(final)):
                if final[i].getEventID() == atd.getEventID():
                    curr = i

            if curr != -1:
                final[curr].incPersons()
            else:
                x = AttentingDTO(atd.getEventID(), -1)
                x.incPersons()
                final.append(x)

        for i in range(len(final)):
            x = self.__eventRepo.find(final[i].getEventID())

            final[i].setEventDesc(x.getDesc())
        return sorted(final, key=lambda e: e.getEventPersons(), reverse=True)
