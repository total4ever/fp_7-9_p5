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
        
    def update(self, person, new_person):
        if person.getID() in self.persons:
            del self.persons[person.getID()]
            
            self.persons[new_person.getID()] = new_person
            
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