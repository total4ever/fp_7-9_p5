from domain.attending import Attending
from domain.dtos import AttentingDTO
class AttendingRepository():
    def __init__(self):
        self.data = []

    def add(self, attending):
        if attending in self.data:
            raise KeyError("Displicate attending.")

        self.data.append(attending)

    def find(self, person, event):
        for atd in self.data:
            if atd.getPersonID() == person and atd.getEventID() == event:
                return atd

        return None

    def test(self):
        return self.data
    # def update(self, attending):
    #     pos = -1
    #     atd = None
    #     for i in range(len(self.__data)):
    #         atd = self.__data[i]
    #         if atd.getEvent() == attending.getEvent() and atd.getPerson() == attending.getPerson():
    #             pos = i
    #
    #     if pos == -1:
    #         raise ValueError("No such association")
    #
    #     self.__data[pos] = attending

    def getAll(self):
        final = []
        for atd in self.data:
            final.append(AttentingDTO(atd.getEventID(), atd.getPersonID()))

        return final

class AttendingRepositoryFile(AttendingRepository):

    def __init__(self, fileName):
        AttendingRepository.__init__(self)
        self.__file = fileName

        try:
            open(self.__file, "r")
        except FileNotFoundError:
            fH = open(self.__file, "w")
            fH.close()


        self.__readFromFile()

    def __saveToFile(self):
        f = open(self.__file, "w")
        for e in self.data:
            f.write(str(e.getEventID()) + "~" + str(e.getPersonID()) +  "\n")

        f.close()

    def __readFromFile(self):

        self.data = []

        with open(self.__file, "r") as fp:
            for line in fp:
                args = line.split("~")
                x = Attending(int(args[0]), int(args[1]))
                self.data.append(x)


    def add(self, x):

        AttendingRepository.add(self, x)
        self.__saveToFile()
