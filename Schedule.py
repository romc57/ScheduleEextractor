import json


class Schedule:
    def __init__(self, json_schedule_file):
        self.day_list_json = None
        self.obj_day_list = list()
        try:
            with open(json_schedule_file) as j_schedule_file:
                self.day_list_json = json.load(j_schedule_file)
        except Exception as e:
            print('Having trouble opening the file\n{}'.format(e))
            exit(-1)
        self.create_day_obj()

    def min_days_arrangement(self):
        pass

    def __len__(self):
        return len(self.obj_day_list)


    def create_day_obj(self):
        for i in range(len(self.day_list_json)):
            pass
