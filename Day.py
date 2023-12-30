from Arrangement import Arrangement


class Day:
    def __init__(self, day_arrangement_dict):
        self.day = day_arrangement_dict['day']
        self.schedule = day_arrangement_dict['schedule']
        self.schedule_obj = list()
        self.create_schedule_obj_lst()

    def create_schedule_obj_lst(self):
        for i in range(len(self.schedule)):
            self.schedule.append(Arrangement(self.schedule[i]))

    def __len__(self):
        return len(self.schedule)



