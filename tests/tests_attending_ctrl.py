from domain.event import Event
from domain.person import Person
from domain.validators import Validators
from repository.attenting_repository import AttendingRepository
from repository.person_repository import PersonRepository
from repository.event_repository import EventRepository
from controller.attenting_ctrl import AttentingCtrl

def tests():
    val = Validators()

    eventRepo = EventRepository()
    personRepo = PersonRepository()
    atdRepo = AttendingRepository()

    ctrl = AttentingCtrl(val, eventRepo, personRepo, atdRepo)
    
    
    p1 = Person(1, "Paul", "Cluj")
    p2 = Person(2, "Vasile", "Cluj")
    e1 = Event(1, "123", "345", "descXY")
    e2 = Event(2, "123", "345", "descJF")
    e3 = Event(3, "123", "345", "descAB")

    personRepo.add(p1)
    personRepo.add(p2)

    eventRepo.add(e1)
    eventRepo.add(e2)
    eventRepo.add(e3)

    ctrl.attend(1, 1)
    ctrl.attend(1, 3)
    ctrl.attend(2, 1)
    ctrl.attend(2, 2)
    ctrl.attend(2, 3)

    try:
        ctrl.attend(1,1)
        assert False
    except KeyError:
        assert True


    for x in ctrl.personEvents(1):
        print(x.getEventDesc())

    for x in ctrl.personsWithMostEvents():
        print(x.getPersonName(), x.getPersonEvents())

    for x in ctrl.eventsWithMostPersons():
        print(x.getEventDesc(), x.getEventPersons())
tests()
