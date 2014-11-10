from domain.person import Person
class PersonCtrl():
    def __init__(self, validator, repo):
        self.__validator = validator
        self.__repo = repo
        
    def addPerson(self, personID, name, addr):
        pers = Person(personID, name, addr)
        
        self.__validator.validate_person(pers)
        self.__repo.add(pers)
    
    def getAll(self):
        return self.__repo.findAll()