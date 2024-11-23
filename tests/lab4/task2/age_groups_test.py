import unittest
from age_groups_for_test import AgeGroups

class AgeGroupsTestCase(unittest.TestCase):

    def test_sort_to_groups(self):
        # given
        people_info1 = [["Даша", "88"],["Маша", "88"], ["Никита", "88"], ["Лёва", "88"]]
        people_info2 = [["Даша", "123"],["Даша", "120"], ["Даша", "122"]]
        people_info3 = [["Даша", "18"], ["Никита", "12"], ["Лёва", "17"], ["Маша", "105"],["Денис", "123"]]
        people_info4 = [["Даша", "150"],]
        people_info5 = [["Амина", "0"], ["Борис", "0"]]

        data1 = AgeGroups()
        data2 = AgeGroups()
        data3 = AgeGroups()
        data4 = AgeGroups()
        data5 = AgeGroups()

        # when
        data1.set_people_info(people_info1)
        data2.set_people_info(people_info2)
        data3.set_people_info(people_info3)
        data4.set_people_info(people_info4)
        data5.set_people_info(people_info5)

        result1 = data1.get_people_ages_statistic()
        result2 = data2.get_people_ages_statistic()
        result3 = data3.get_people_ages_statistic()
        result4 = data4.get_people_ages_statistic()
        result5 = data5.get_people_ages_statistic()

        print(result3)
        # then
        self.assertEqual(result1, ['Люди до 100 лет: Даша (88), Маша (88), Никита (88), Лёва (88)'])
        self.assertEqual(result2, ['Люди до 123 лет: Даша (123), Даша (122), Даша (120)'])
        self.assertEqual(result3, ['Люди до 123 лет: Денис (123), Маша (105)','Люди до 18 лет: Даша (18), Лёва (17), Никита (12)'])
        self.assertEqual(result4, [])
        self.assertEqual(result5, ['Люди до 18 лет: Амина (0), Борис (0)'])


if __name__ == "__main__":
    unittest.main()