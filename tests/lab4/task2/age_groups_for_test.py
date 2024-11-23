class AgeGroups:
    ages = ["18", "25", "35", "45", "60", "80", "100"]
    people_info = []

    def __init__(self):
        self.ages = ["-1"] + self.ages + ["123"]
        self.ages = self.age_to_age_list()
        self.age_groups = [[] for i in range(len(self.ages))]

    def set_people_info(self, lst:list):
        """Функция для тестов"""
        self.people_info = lst

    def age_to_age_list(self):
        """Генерирует из числа промежуток всех натуральных чисел(с 0) от и до этого числа"""
        result = []
        for age in range(1, len(self.ages)):
            result.append([str(el) for el in list(range(int(self.ages[age - 1]) + 1, int(self.ages[age]) + 1))])

        return result

    def get_info(self):
        """Выводит данные, которые ввёл пользователь(в консоль)"""
        print(f"Список полученных людей: {self.people_info}")

    def people_to_age_groups(self):
        """ Распределяет людей по возрастным группам"""
        for person in self.people_info:
            for age in range(len(self.ages)):
                if person[-1] in self.ages[age]:
                    self.age_groups[age].append(person)
                    break

    def sort_people_in_ages_groups(self):
        """ Сортирует людей в возрастных группах в порядке убывания их возраста"""
        for group in range(len(self.age_groups)):
            self.age_groups[group] = sorted(self.age_groups[group], key=lambda x:x[-1], reverse=True)

    def lst_to_string_description(self, lst:list[str, str]):
        """ Переделывает список данных о человеке в строку"""
        return f"{lst[0]} ({lst[-1]})"

    def get_people_ages_statistic(self):
        """ Выводит результаты о группах людей разной категории возрастов"""
        result = []
        self.people_to_age_groups()
        self.sort_people_in_ages_groups()
        for group in range(len(self.age_groups)-1, -1, -1):
            group_result = [f"Люди до {self.ages[group][-1]} лет: "]
            for person in self.age_groups[group]:
                 group_result.append(self.lst_to_string_description(person) + ", ")
            if group_result[1:]:
                result.append(("".join(group_result)[:-2]))

        return result