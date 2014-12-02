from domain.person import Person

import unittest

class Tests(unittest.TestCase):
    def test1(self):
        pers = Person(1, "Paul", "Cluj")

        self.assertEqual(pers.getID(), 1)
        self.assertEqual(pers.getName(), "Paul")
        self.assertEqual(pers.getAddr(), "Cluj")
