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
        
    def update(self, event, new_event):
        if event.getID() in self.events:
            del self.events[event.getID()]
            
            self.events[new_event.getID()] = new_event
            
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