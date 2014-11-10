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

