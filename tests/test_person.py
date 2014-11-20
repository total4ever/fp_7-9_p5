from domain.person import Person
def tests():
    pers = Person(1, "Paul", "Cluj")
    
    assert pers.getID() == 1
    assert pers.getName() == "Paul"
    assert pers.getAddr() == "Cluj"
    
    pers.setID(5)
    assert pers.getID() == 5
    
    pers.setName("Paula")
    assert pers.getName() == "Paula"
    
    pers.setAddr("Cluj-Napoca")
    assert pers.getAddr() == "Cluj-Napoca"

tests()