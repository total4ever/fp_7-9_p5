from domain.person import Person


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
    def update(self, person, new_person):
        personID = person.getID()
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


class PersonRepositoryFile(PersonRepository):
    def __init__(self, fileName):
        PersonRepository.__init__(self)
        self.__file = fileName

        try:
            open(self.__file, "r")
        except FileNotFoundError:
            fH = open(self.__file, "w")
            fH.close()


        self.__readFromFile()



    def __saveToFile(self):
        f = open(self.__file, "w")

        for e in self.persons:
            x = self.persons[e]
            f.write(str(x.getID()) + "~" + x.getName() + "~" + x.getAddr() + "\n")

        f.close()

    def __readFromFile(self):

        self.persons = {}
        with open(self.__file, "r") as fp:
            for line in fp:
                args = line.split("~")
                x = Person(int(args[0]), args[1], args[2].strip())
                self.persons[x.getID()] = x


    def add(self, event):
        PersonRepository.add(self, event)
        self.__saveToFile()

    def remove(self, ID):
        PersonRepository.remove(self, ID)
        self.__saveToFile()

    def update(self, eventID, new_event):
        PersonRepository.update(self, eventID, new_event)
        self.__saveToFile()
