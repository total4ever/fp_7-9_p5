from domain.validators import Validators
from repository.person_repository import PersonRepository
from controller.person_ctrl import PersonCtrl
from ui.console import Console

val = Validators()
person_repo = PersonRepository()
person_ctrl = PersonCtrl(val, person_repo)

cons = Console(person_ctrl)
cons.startUI()