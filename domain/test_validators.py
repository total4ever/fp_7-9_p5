from domain.person import Person
from domain.validators import Validators
from domain.event import Event
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

def testValidateEvent():
    validator = Validators()
    
    evt = Event(-1, "18/03/2010", "18.05", "Eveniment?")   
    try:
        validator.validate_event(evt)
        assert False
    except ValueError:
        assert True
    
    
    evt = Event(1, "", "18.05", "Eveniment?")   
    try:
        validator.validate_event(evt)
        assert False
    except ValueError:
        assert True

        
testValidatePerson()
testValidateEvent()
        
    
    