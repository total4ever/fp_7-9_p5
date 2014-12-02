from domain.attending import Attending
from domain.event import Event
from domain.person import Person

import unittest

class Tests(unittest.TestCase):
    def testCreate(self):
        atd = Attending(1, 5)

        self.assertEqual(atd.getEventID(), 5)
        self.assertEqual(atd.getPersonID(), 1)

    def testEq(self):
        a1 = Attending(1, 2)
        a2 = Attending(1, 2)
        a3 = Attending(1, 8)
        self.assertEqual(a1, a2)
        self.assertNotEqual(a1, a3)
