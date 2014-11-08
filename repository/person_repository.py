class PersonRepository():
    def __init__(self):
        self.persons = {}
    
    def add(self, person):
        if person.getID() in self.persons:
            raise KeyError("Duplicate person entry for ID " + person.getID())
        
        self.persons[person.getID()] = person
    
    def remove(self, person):
        if person.getID() in self.persons:
            del self.persons[person.getID()]
        
    def update(self, person, new_person):
        if person.getID() in self.persons:
            self.persons[person.getID()] = new_person
        else:
            raise KeyError("No person with ID " + person.getID() + " found")
            
    def find(self, ID):
        if ID in self.persons:
            return self.persons[ID]
        else:
            return None
        
    def findAll(self):
        return self.persons
