import json


class Schedule:
    def __init__(self, json_schedule_file):
        self.day_list_json = None
        try:
            with open(json_schedule_file) as j_schedule_file:
                self.day_list_json = json.load(j_schedule_file)
        except Exception as e:
            print('Having trouble opening the file\n{}'.format(e))
            exit(-1)
        self.obj_day_list = list()
        self.create_day_obj()

    def create_day_obj(self):
        for i in range(len(self.day_list_json)):
            self.obj_day_list.append(self, self.obj_day_list[i])
