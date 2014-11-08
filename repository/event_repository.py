class EventRepository():
    def __init__(self):
        self.events = {}
    
    def add(self, event):
        if event.getID() in self.events:
            raise KeyError("Duplicate event entry for ID " + event.getID())
        
        self.events[event.getID()] = event
    
    def remove(self, event):
        if event.getID() in self.events:
            del self.events[event.getID()]
        
    def update(self, event, new_event):
        if event.getID() in self.persons:
            self.events[event.getID()] = new_event
        else:
            raise KeyError("No event with ID " + event.getID() + " found")
            
    def find(self, ID):
        if ID in self.events:
            return self.events[ID]
        else:
            return None
        
    def findAll(self):
        return self.events
