
class Validators():
    
    def validate_person(self, pers):
        if pers.getID() < 0:
            raise ValueError("Negative person ID.")
        if pers.getName() == "":
            raise ValueError("Empty person name.")
        if pers.getAddr() == "":
            raise ValueError("Empty person address.")

