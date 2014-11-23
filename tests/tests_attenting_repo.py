from repository.attenting_repository import AttendingRepository
from domain.person import Person
from domain.event import Event
from domain.attending import Attending

def tests():
    repo = AttendingRepository()

    p1 = Person(1, "Paul", "Cluj")
    e1 = Event(5, "09/11/2015", "17.30", "Epic ceva?")

    atd = Attending(p1, e1)
    repo.add(atd)


    assert repo.find(p1, e1) == atd

    all = repo.getAll()
    assert all[0].getPersonID() == 1
    assert all[0].getEventID() == 5

tests()
