from domain.person import Person
from domain.validators import Validators
def testValidatePerson():
    validator = Validators()
    
    pers = Person(-1, "Ion", "Cluj")   
    try:
        validator.validate_person(pers)
        assert False
    except ValueError:
        assert True
    
    
    pers = Person(1, "", "Cluj") 
    try:
        validator.validate_person(pers)
        assert False
    except ValueError:
        assert True
      
        
    pers = Person(1, "Ion", "")
    try:
        validator.validate_person(pers)
        assert False
    except ValueError:
        assert True

testValidatePerson()
        
    
    