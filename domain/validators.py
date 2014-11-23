class Validators():
    
    def validate_person(self, pers):
        errors = []
        if pers.getID() < 0:
            errors.append("Negative person ID.")
        if pers.getName() == "":
            errors.append("Empty person name.")
        if pers.getAddr() == "":
            errors.append("Empty person address.")
        
        if errors != []:
            raise ValueError(errors)

    def validate_event(self, event):
        errors = []
        if event.getID() < 0:
            errors.append("Negative event ID.")
        if event.getDate() == "":
            errors.append("Empty event date.")
        if event.getTime() == "":
            errors.append("Empty event time.")
        if event.getDesc() == "":
            errors.append("Empty event description.")

        if errors != []:
            raise ValueError(errors)

    def validate_attenting(self, attenting):
        errors = []

        if attenting.getEvent() == None:
            errors.append("Empty event")

        if attenting.getPerson() == None:
            errors.append("Empty person")


        if errors != []:
            raise ValueError(errors)
