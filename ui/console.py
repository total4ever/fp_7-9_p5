class Console():
    def __init__(self, pctrl, ectrl):
        self.__person_ctrl = pctrl
        self.__event_ctrl = ectrl
    
    def printMenu(self):
        print("1. Adauga persoana")
        print("2. Afisare persoane")
        print("3. Adauga eveniment")
        print("4. Afisare evenimente")
        print("5. Stergere persoana")
        print("6. Stergere eveniment")
        print("7. Modificare persoana")
        print("8. Modificare eveniment")
        print("q. Iesire")
        
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

    def __showAllPersons(self):
        lst = self.__person_ctrl.getAll()
        
        for value in lst:
            p = lst[value]
            print(p.getID(), " -> ", p.getName(), "|", p.getAddr())
        
    def __deletePerson(self):
        personID = int(input("ID: "))
        try:
            self.__person_ctrl.removePerson(personID)
        except KeyError:
            print("ID persoana inexistent.")
    
    def __updatePerson(self):
        personID = int(input("ID: "))
        
        newname = input("Nume: ")
        newaddr = input("Adresa: ")
        try:
            self.__person_ctrl.updatePerson(personID, newname, newaddr)
        except KeyError:
            print("ID persoana inexistent.")
    
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

    def __showAllEvents(self):
        lst = self.__event_ctrl.getAll()

        for value in lst:
            p = lst[value]
            print(p.getID(), " -> ", p.getDate(), "at", p.getTime(), " | ", p.getDesc())
       
    def __deleteEvent(self):
        eventID = int(input("ID: "))
        try:
            self.__event_ctrl.removeEvent(eventID)
        except KeyError:
            print("ID eveniment deja inexistent.")
    def __updateEvent(self):
        eventID = int(input("ID: "))
        
        newdate = input("Data: ")
        newtime = input("Ora: ")
        newdesc = input("Descriere: ")
        
        try:
            self.__event_ctrl.updateEvent(eventID, newdate, newtime, newdesc)
        except KeyError:
            print("ID eveniment deja inexistent.")
            
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
            if cmd == "5":
                self.__deletePerson()
            if cmd == "6":
                self.__deleteEvent()
            if cmd == "7":
                self.__updatePerson()
            if cmd == "8":
                self.__updateEvent()

            if cmd == "q":
                break
