from domain.validators import Validators
from repository.person_repository import PersonRepository
from controller.person_ctrl import PersonCtrl
from repository.event_repository import EventRepository
from controller.event_ctrl import EventCtrl
from domain.event import Event


def testEvent():
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
    
    ctrl.updateEvent(1, "123", "456", "789")
    assert ctrl.getAll()[1] == Event(1, "123", "456", "789")
    
    ctrl.removeEvent(1)
    assert len(ctrl.getAll()) == 0
        
testEvent()