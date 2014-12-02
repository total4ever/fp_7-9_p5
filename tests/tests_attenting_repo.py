from repository.attenting_repository import AttendingRepositoryFile
from domain.attending import Attending

import unittest

class Tests(unittest.TestCase):

    def test1(self):
        f = open("atd.txt", "w")
        f.close()
        repo = AttendingRepositoryFile("atd.txt")

        atd = Attending(1, 5)
        repo.add(atd)

        #assert repo.find(1, 5) == atd
        self.assertEqual(repo.find(1,5), atd)

        all = repo.getAll()

        self.assertEqual(all[0].getPersonID(), 1)
        self.assertEqual(all[0].getEventID(), 5)

