from repository.person_repository import PersonRepository
from domain.person import Person
def testPerson():
    rep = PersonRepository()
    
    # Add
    rep.add(Person(1, "Paul", "Cluj"))  
    rep.add(Person(2, "Gheorghe", "Cluj"))
    
    # Check if added
    assert rep.getEntriesNum() == 2
    
    # Should raise exception for duplicate key
    try:
        rep.add(Person(1, "Paul2", "Cluj"))
        assert False
    except KeyError:
        assert True

    # If and exception was raised it shouldn't add it to the repository
    assert rep.getEntriesNum() == 2
    
    # Find by ID
    assert rep.find(2) == Person(2, "Gheorghe", "Cluj")
    
    # Update
    rep.update(Person(2, "Gheorghe", "Cluj"), Person(8, "Ana", "Cluj"))
    assert rep.find(8) == Person(8, "Ana", "Cluj")
    
    # Delete
    rep.remove(8)
    assert rep.find(8) == None


testPerson()