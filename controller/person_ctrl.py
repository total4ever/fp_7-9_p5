from domain.person import Person


class PersonCtrl():
    def __init__(self, validator, repo):
        self.__validator = validator
        self.__repo = repo

    def addPerson(self, personID, name, addr):
        pers = Person(personID, name, addr)

        self.__validator.validate_person(pers)
        self.__repo.add(pers)

    def removePerson(self, personID):
        self.__repo.remove(personID)

    def updatePerson(self, personID, newname, newaddr):
        self.__repo.update(personID, Person(personID, newname, newaddr))

    def getAll(self):
        return self.__repo.findAll()