from domain.dtos import AttentingDTO
class AttendingRepository():
    def __init__(self):
        self.__data = []

    def add(self, attending):
        if attending in self.__data:
            raise KeyError("Displicate attending.")

        self.__data.append(attending)

    def find(self, person, event):
        for atd in self.__data:
            if atd.getPerson() == person and atd.getEvent() == event:
                return atd

        return None

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
        for atd in self.__data:
            final.append(AttentingDTO(atd.getEvent().getID(), atd.getPerson().getID()))

        return final
