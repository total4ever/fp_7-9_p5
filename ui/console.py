class Console():
    def __init__(self, pctrl, ectrl, actrl):
        self.__person_ctrl = pctrl
        self.__event_ctrl = ectrl
        self.__attend_ctrl = actrl
    def printMenu(self):
        print("1. Adauga persoana")
        print("2. Afisare persoane")
        print("3. Adauga eveniment")
        print("4. Afisare evenimente")
        print("5. Stergere persoana")
        print("6. Stergere eveniment")
        print("7. Modificare persoana")
        print("8. Modificare eveniment")

        print("9. Adauga persoana la eveniment")
        
        print("r1. Evenimentele la care participa o persoana")
        print("r2. Persoanele care participa la cele mai multe evenimente")
        print("r3. Evenimentele la care participa cele mai multe persoane")
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

    def __attend(self):
        personID = int(input("ID persoana: "))
        eventID = int(input("ID eveniment:"))

        try:
            self.__attend_ctrl.attend(personID, eventID)
            print("OK")
        except ValueError as msg:
            print(msg)

    def __personEvents(self):
        personID = int(input("ID persoana: "))

        try:
            data = self.__attend_ctrl.personEvents(personID)
            for x in data:
                print(x.getEventDesc())
        except ValueError as msg:
            print(msg)

    def __personsWithMostEvents(self):
        data = self.__attend_ctrl.personsWithMostEvents()
        for x in data:
            print(x.getPersonName(), x.getPersonEvents())

    def __eventsWithMostPersons(self):
        data = self.__attend_ctrl.eventsWithMostPersons()

        for x in data:
            print(x.getEventDesc(), x.getEventPersons())

    def startUI(self):
        self.__person_ctrl.addPerson(1, "Paul", "Cluj")
        self.__person_ctrl.addPerson(2, "Paula", "Cluj")
        self.__person_ctrl.addPerson(3, "Ion", "Cluj")
        self.__person_ctrl.addPerson(4, "Gheorghe", "Cluj")

        self.__event_ctrl.addEvent(1, "09/11/2014", "18.05", "eveniment 1")
        self.__event_ctrl.addEvent(2, "09/11/2014", "18.05", "eveniment 2")
        self.__event_ctrl.addEvent(3, "09/11/2014", "18.05", "eveniment 3")
        self.__event_ctrl.addEvent(4, "09/11/2014", "18.05", "eveniment 4")
        self.__event_ctrl.addEvent(5, "09/11/2014", "18.05", "eveniment 5")
        self.__event_ctrl.addEvent(6, "09/11/2014", "18.05", "eveniment 6")

        self.__attend_ctrl.attend(1, 1)
        self.__attend_ctrl.attend(1, 2)
        self.__attend_ctrl.attend(1, 3)

        self.__attend_ctrl.attend(2, 1)
        self.__attend_ctrl.attend(2, 3)

        self.__attend_ctrl.attend(3, 4)
        self.__attend_ctrl.attend(3, 5)
        self.__attend_ctrl.attend(3, 6)

        self.__attend_ctrl.attend(4, 1)
        self.__attend_ctrl.attend(4, 2)
        self.__attend_ctrl.attend(4, 3)
        self.__attend_ctrl.attend(4, 4)
        self.__attend_ctrl.attend(4, 5)

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
            if cmd == "9":
                self.__attend()


            if cmd == "r1":
                self.__personEvents()
            if cmd == "r2":
                self.__personsWithMostEvents()
            if cmd == "r3":
                self.__eventsWithMostPersons()

            if cmd == "q":
                break
