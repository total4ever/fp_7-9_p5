class Console():
    def __init__(self, pctrl):
        self.__person_ctrl = pctrl
    
    def printMenu(self):
        print("1. Adauga persoana")
        print("2. Afisare persoane")
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
       
    def __showAllPersons(self):
        lst = self.__person_ctrl.getAll()
        
        for value in lst:
            p = lst[value]
            print(p.getID(), " -> ", p.getName(), "|", p.getAddr())
        
    def startUI(self):
        while True: 
            cmd = input("Comanda:")
            if cmd == "1":
                self.__addPerson()
            if cmd == "2":
                self.__showAllPersons()
            if cmd == "x":
                break
