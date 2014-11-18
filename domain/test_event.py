from domain.event import Event
def tests():
    evt = Event(1, "20/10/2015", "17.09", "Bday")
    
    assert evt.getID() == 1
    assert evt.getDate() == "20/10/2015"
    assert evt.getTime() == "17.09"
    assert evt.getDesc() == "Bday"
    
    evt.setID(5)
    assert evt.getID() == 5
    
    evt.setDate("1345")
    assert evt.getDate() == "1345"
    
    evt.setTime("18.09")
    assert evt.getTime() == "18.09"
    
    evt.setDesc("new desc")
    assert evt.getDesc() == "new desc"
    
tests()