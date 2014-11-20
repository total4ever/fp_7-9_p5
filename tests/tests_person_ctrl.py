from domain.validators import Validators
from repository.person_repository import PersonRepository
from controller.person_ctrl import PersonCtrl
from domain.person import Person


def testAddPerson():
    val = Validators()
    repo = PersonRepository()
    
    ctrl = PersonCtrl(val, repo)
    
    ctrl.addPerson(1, "Paul", "Cluj")
    
    assert len(ctrl.getAll()) == 1
    
    
    try:
        ctrl.addPerson(1, "Paul", "Cluj")
        assert False
    except KeyError:
        assert True
        
    try:
        ctrl.addPerson(-5, "Paul", "Cluj")
        assert False
    except ValueError:
        assert True
        
    ctrl.updatePerson(1, "Andrei", "Bucuresti")
    assert ctrl.getAll()[1] == Person(1, "Andrei", "Bucuresti")
    
    ctrl.removePerson(1)
    assert len(ctrl.getAll()) == 0
testAddPerson()