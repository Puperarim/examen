import random
from re import fullmatch

class InvalidDateFormat(Exception):
    pass

class Stage:
    pattern = r'^\d{2}\.\d{2}\.\d{4}$'

    def __init__(self, cost, start_date, end_date, description, status):
        self.__cost = cost
        self.start_date = start_date
        self.end_date = end_date
        self.__description = description
        self.__status = status
        self.__prev_stage = None
        self.__next_stage = None

    @property
    def cost(self):
        return self.__cost

    @property
    def start_date(self):
        return self.__start_date

    @start_date.setter
    def start_date(self, date_str):
        if not fullmatch(Stage.pattern, date_str):
            raise InvalidDateFormat('Неверный формат даты')
        self.__start_date = date_str

    @property
    def end_date(self):
        return self.__end_date

    @end_date.setter
    def end_date(self, date_str):
        if not fullmatch(Stage.pattern, date_str):
            raise InvalidDateFormat('Неверный формат даты')
        self.__end_date = date_str

    @property
    def description(self):
        return self.__description

    @property
    def status(self):
        return self.__status

    @property
    def prev_stage(self):
        return self.__prev_stage

    @prev_stage.setter
    def prev_stage(self, stage):
        self.__prev_stage = stage

    @property
    def next_stage(self):
        return self.__next_stage

    @next_stage.setter
    def next_stage(self, stage):
        self.__next_stage = stage

    def next(self):
        return self.next_stage

    def prev(self):
        return self.prev_stage

    def start(self):
        self.__status = "осуществляется"
        print(f'Статус стройки изменен на {self.status}')

    def stop(self):
        self.__status = "выполнен"
        print(f'Статус стройки изменен на {self.status}')

    def reject(self):
        self.__status = "забракован"
        print(f'Статус стройки изменен на {self.status}')

class Project(Stage):
    pass

class Foundation(Stage):
    pass

class Walls(Stage):
    pass

class Roof(Stage):
    pass

class Finishing(Stage):
    pass

class Construction:
    def __init__(self, stage_first):
        self.__stage_first = stage_first

    @property
    def stage_first(self):
        return self.__stage_first

    @stage_first.setter
    def stage_first(self, stage):
        self.__stage_first = stage

    def run(self):
        current_stage = self.stage_first
        while current_stage:
            if random.randint(1, 10) == 1:
                current_stage.reject()
                if current_stage.prev():
                    current_stage = current_stage.prev()
                else:
                    return "Стройка отменена: проект забракован."
            else:
                current_stage.start()
                current_stage = current_stage.next()
        return "Стройка успешно завершена."


try:
    project = Project(1000, "11.11.1111", "11.11.1111", "Проект", "запланирован")
    foundation = Foundation(5000, "11.11.1111", "11.11.1111", "Фундамент", "запланирован")
    walls = Walls(7000, "11.11.1111", "11.11.1111", "Стены", "запланирован")
    roof = Roof(8000, "11.11.1111", "11.11.1111", "Крыша", "запланирован")
    finishing = Finishing(4000, "11.11.1111", "11.11.1111", "Отделка", "запланирован")

    project.next_stage = foundation
    foundation.prev_stage = project
    foundation.next_stage = walls
    walls.prev_stage = foundation
    walls.next_stage = roof
    roof.prev_stage = walls
    roof.next_stage = finishing
    finishing.prev_stage = roof

    construction = Construction(project)

    successful_cases = 0
    for i in range(1000):
        if construction.run() == "Стройка успешно завершена.":
            successful_cases += 1

    success_rate = successful_cases / 1000 * 100
    print(f"Вероятность успешного завершения: {success_rate}%")
except InvalidDateFormat as e:
    print(e)


class TestInvalidDateFormat:
    @staticmethod
    def run_test():
        try:
            Stage(1000, "11111111", "11.11.1111", "Тест", "запланирован")
        except InvalidDateFormat as e:
            print(e)

test = TestInvalidDateFormat
test.run_test()