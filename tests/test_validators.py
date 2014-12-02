from domain.person import Person
from domain.validators import Validators
from domain.event import Event

import unittest

class Tests(unittest.TestCase):
    def testValidatePerson(self):
        validator = Validators()

        pers = Person(-1, "Ion", "Cluj")
        self.assertRaises(ValueError, validator.validate_person, pers)

        pers = Person(1, "", "Cluj")
        self.assertRaises(ValueError, validator.validate_person, pers)

        pers = Person(1, "Ion", "")
        self.assertRaises(ValueError, validator.validate_person, pers)

    def testValidateEvent(self):
        validator = Validators()

        evt = Event(-1, "18/03/2010", "18.05", "Eveniment?")
        self.assertRaises(ValueError, validator.validate_event, evt)

        evt = Event(1, "", "18.05", "Eveniment?")
        self.assertRaises(ValueError, validator.validate_event, evt)