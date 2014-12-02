from domain.event import Event
import unittest

class Tests(unittest.TestCase):
    def test1(self):
        evt = Event(1, "20/10/2015", "17.09", "Bday")

        self.assertEqual(evt.getID(), 1)
        self.assertEqual(evt.getDate(), "20/10/2015")
        self.assertEqual(evt.getTime(), "17.09")
        self.assertEqual(evt.getDesc(), "Bday")

        evt.setID(5)
        self.assertTrue(evt.getID(), 5)