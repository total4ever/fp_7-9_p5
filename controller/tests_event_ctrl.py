from domain.validators import Validators
from repository.person_repository import PersonRepository
from controller.person_ctrl import PersonCtrl
from repository.event_repository import EventRepository
from controller.event_ctrl import EventCtrl


def testAddEvent():
    val = Validators()
    repo = EventRepository()
    
    ctrl = EventCtrl(val, repo)
    
    ctrl.addEvent(1, "17/04/2014", "18.30", "Mai epic")
    
    assert len(ctrl.getAll()) == 1
    
    
    try:
        ctrl.addEvent(1, "17/04/2014", "17.30", "Epic")
        assert False
    except KeyError:
        assert True
        
    try:
        ctrl.addEvent(-1, "17/04/2014", "", "Epic")
        assert False
    except ValueError:
        assert True
        
testAddEvent()