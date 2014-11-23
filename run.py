from controller.attenting_ctrl import AttentingCtrl
from domain.validators import Validators
from repository.attenting_repository import AttendingRepository
from repository.person_repository import PersonRepository
from controller.person_ctrl import PersonCtrl
from ui.console import Console
from repository.event_repository import EventRepository
from controller.event_ctrl import EventCtrl

val = Validators()
person_repo = PersonRepository()
person_ctrl = PersonCtrl(val, person_repo)

event_repo = EventRepository()
event_ctrl = EventCtrl(val, event_repo)

attend_repo = AttendingRepository()
attend_ctrl = AttentingCtrl(val, event_repo, person_repo, attend_repo)

cons = Console(person_ctrl, event_ctrl, attend_ctrl)
cons.startUI()