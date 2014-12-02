from domain.validators import Validators
from repository.event_repository import EventRepository
from controller.event_ctrl import EventCtrl
from domain.event import Event

import unittest

class Tests(unittest.TestCase):

    def test1(self):
        val = Validators()
        repo = EventRepository()

        ctrl = EventCtrl(val, repo)

        ctrl.addEvent(1, "17/04/2014", "18.30", "Mai epic")

        self.assertEqual(len(ctrl.getAll()), 1)

        self.assertRaises(KeyError, ctrl.addEvent, 1, "17/04/2014", "17.30", "Epic")

        self.assertRaises(ValueError, ctrl.addEvent, -1, "17/04/2014", "", "Epic")

        ctrl.updateEvent(1, "123", "456", "789")
        self.assertEqual(ctrl.getAll()[1], Event(1, "123", "456", "789"))

        ctrl.removeEvent(1)