from repository.event_repository import EventRepository
from domain.event import Event

def testEvent():
    rep = EventRepository()
    
    # Add
    rep.add(Event(1, "24/7/2014", "18:00", "epic event!!"))  
    rep.add(Event(2, "24/11/2014", "00:00", "bday!"))
    
    # Check if added
    assert rep.getEntriesNum() == 2
    
    # Should raise exception for duplicate key
    try:
        rep.add(Event(2, "24/7/2014", "18:00", "epic event!!"))
        assert False
    except KeyError:
        assert True

    # If and exception was raised it shouldn't add it to the repository
    assert rep.getEntriesNum() == 2
    
    # Find by ID
    assert rep.find(2) == Event(2, "24/11/2014", "00:00", "bday!")
    
    # Update
    rep.update(Event(2, "24/11/2014", "00:00", "bday!"), Event(5, "18/11/2015", "24:00", "other stuff :("))
    assert rep.find(5) == Event(5, "18/11/2015", "24:00", "other stuff :(")
    
    # Delete
    rep.remove(8)
    assert rep.find(8) == None
    

testEvent()