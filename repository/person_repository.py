class PersonRepository():
    def __init__(self):
        self.persons = {}
    
    def add(self, person):
        if person.getID() in self.persons:
            raise KeyError("Duplicate person entry for ID")
        
        self.persons[person.getID()] = person
    
    def remove(self, ID):
        if ID in self.persons:
            del self.persons[ID]
        else:
            raise KeyError
    def update(self, personID, new_person):
        if personID in self.persons:
            self.persons[personID] = new_person
            
        else:
            raise KeyError("No person with specified ID found")
            
    def find(self, ID):
        if ID in self.persons:
            return self.persons[ID]
        else:
            return None
        
    def findAll(self):
        return self.persons

    def getEntriesNum(self):
        return len(self.persons)