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
        
    def update(self, eventID, new_event):
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