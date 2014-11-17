class Console():
    def __init__(self, pctrl, ectrl):
        self.__person_ctrl = pctrl
        self.__event_ctrl = ectrl
    
    def printMenu(self):
        print("1. Adauga persoana")
        print("2. Afisare persoane")
        print("3. Adauga eveniment")
        print("4. Afisare evenimente")
        print("x. Iesire")
        
    def __addPerson(self):
        personID = int(input("ID: "))
        name = input("Nume: ")
        addr = input("Adresa: ")
        
        try:
            self.__person_ctrl.addPerson(personID, name, addr)
        except KeyError:
            print("ID persoana deja existent.")
        except ValueError as msg:
            print(msg)

    def __addEvent(self):
        eventID = int(input("ID: "))
        date = input("Data: ")
        time = input("Ora: ")
        desc = input("Desriere: ")

        try:
            self.__event_ctrl.addEvent(eventID, date, time, desc)
        except KeyError:
            print("ID eveniment deja existent.")
        except ValueError as msg:
            print(msg)

    def __showAllPersons(self):
        lst = self.__person_ctrl.getAll()
        
        for value in lst:
            p = lst[value]
            print(p.getID(), " -> ", p.getName(), "|", p.getAddr())

    def __showAllEvents(self):
        lst = self.__event_ctrl.getAll()

        for value in lst:
            p = lst[value]
            print(p.getID(), " -> ", p.getDate(), "at", p.getTime(), " | ", p.getDesc())
        
    def startUI(self):
        while True:
            self.printMenu()

            cmd = input("Comanda:")
            if cmd == "1":
                self.__addPerson()
            if cmd == "2":
                self.__showAllPersons()
            if cmd == "3":
                self.__addEvent()
            if cmd == "4":
                self.__showAllEvents()

            if cmd == "x":
                break
