from domain.event import Event


class EventRepository():
    def __init__(self):
        self.events = {}
    
    def add(self, event):
        if event.getID() in self.events:
            raise KeyError("Duplicate event entry")
        
        self.events[event.getID()] = event
    
    def remove(self, ID):
        if ID in self.events:
            del self.events[ID]
        else:
            raise KeyError()
        
    def update(self, event, new_event):
        eventID = event.getID()
        if eventID in self.events:
            self.events[eventID] = new_event
            
        else:
            raise KeyError("No person with specified ID found")
            
    def find(self, ID):
        if ID in self.events:
            return self.events[ID]
        else:
            return None
        
    def findAll(self):
        return self.events

    def getEntriesNum(self):
        return len(self.events)



class EventRepositoryFile(EventRepository):
    def __init__(self, fileName):
        EventRepository.__init__(self)
        self.__file = fileName

        try:
            open(self.__file, "r")
        except FileNotFoundError:
            fH = open(self.__file, "w")
            fH.close()


        self.__readFromFile()



    def __saveToFile(self):
        f = open(self.__file, "w")

        for e in self.events:
            event = self.events[e]
            f.write(str(event.getID()) + "~" + event.getDate() + "~" + event.getTime() + "~" + event.getDesc() + "\n")

        f.close()

    def __readFromFile(self):

        self.events = {}
        with open(self.__file, "r") as fp:
            for line in fp:
                args = line.split("~")
                x = Event(int(args[0]), args[1], args[2], args[3].strip())
                self.events[x.getID()] = x


    def add(self, event):
        EventRepository.add(self, event)
        self.__saveToFile()

    def remove(self, ID):
        EventRepository.remove(self, ID)
        self.__saveToFile()

    def update(self, eventID, new_event):
        EventRepository.update(self, eventID, new_event)
        self.__saveToFile()
