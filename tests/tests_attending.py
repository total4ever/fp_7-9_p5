from domain.attending import Attending
from domain.event import Event
from domain.person import Person


def testCreate():
    event = Event(1, "24/11/2014", "00.00", "bday!")
    person = Person(1, "Paul", "Cluj")

    atd = Attending(person, event)
    assert atd.getEvent() == event
    assert atd.getPerson() == person


def testEq():
    event = Event(1, "24/11/2014", "00.00", "bday!")
    person = Person(1, "Paul", "Cluj")

    atd1 = Attending(person, event)
    atd2 = Attending(person, event)
    assert atd1 == atd2

    atd3 = Attending(Person(2, "Ioan", "Cluj"), event)
    assert atd1 != atd3


testCreate()
testEq()
