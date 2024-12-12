import unittest
from src.lab5.product_market_orders import Order, Utils


class OrderValidationTestCase(unittest.TestCase):

    def test_order_validate(self):
        # given
        correct_number = "+7-981-632-12-21"
        correct_address = "Россия. Ленинградская область. Санкт-Петербург. Савушкина"
        incorrect_number = "+8-131-234-5678"
        incorrect_address = "Япония.Шибуя.Шибуя - кроссинг"
        correct_order = Order("31987", "Сыр, Колбаса, Сыр, Макароны, Колбаса", "Петрова Анна", correct_address, correct_number, "MIDDLE")
        incorrect_order = Order("31987", "Сыр, Колбаса, Сыр, Макароны, Колбаса", "Петрова Анна", incorrect_address,
                              incorrect_number, "MIDDLE")

        # when
        non_errors = correct_order.validate()
        errors = incorrect_order.validate()

        # then
        self.assertEqual(non_errors, [])
        self.assertEqual(errors, [(1, 'Япония.Шибуя.Шибуя - кроссинг'), (2, '+8-131-234-5678')])


    def test_formatted_products(self):
        # given
        utils = Utils("orders.txt","order_country.txt", "non_valid_orders.txt")
        orders = utils.read_orders()
        order1 = orders[0]
        order2 = orders[1]
        order3 = orders[2]
        order4 = orders[3]
        order5 = orders[4]

        # when
        products1 = order1.formatted_products()
        products2 = order2.formatted_products()
        products3 = order3.formatted_products()
        products4 = order4.formatted_products()
        products5 = order5.formatted_products()

        # then
        self.assertEqual(products1, 'Сыр x2, Колбаса x2, Макароны x1')
        self.assertEqual(products2, 'Молоко x2, Яблоки x2, Хлеб x1')
        self.assertEqual(products3, 'Сыр x2, Колбаса x2, Макароны x1')
        self.assertEqual(products4, 'Хлеб x2, Молоко x2')
        self.assertEqual(products5, 'Яблоки x2, Макароны x1')


    def test_read_orders(self):
        # given
        utils = Utils("orders.txt","order_country.txt", "non_valid_orders.txt")

        # when
        orders = utils.read_orders()

        # then
        self.assertEqual(str(type(orders[0])), "<class 'src.lab5.product_market_orders.Order'>")
        self.assertEqual(len(orders), 9)

    def test_sort_key(self):
        # given
        utils = Utils("orders.txt", "order_country.txt", "non_valid_orders.txt")
        orders = utils.read_orders()
        order1 = orders[3]
        order2 = orders[1]
        valid_orders = [order1, order2]
        print('\n', order1, order2) # Чтобы показать, что не отсортированы по стране

        # Функция для сортировки по стране и приоритету
        def sort_key(order):
            country = order.delivery_address.split('.')[0]
            priority = {'MAX': 1, 'MIDDLE': 2, 'LOW': 3}[order.delivery_priority]

            if country == 'Российская Федерация' or "Ленинградская область" or "Московская область":
                return '', priority
            return country, priority

        # when
        valid_orders.sort(key=sort_key)

        # then
        # Тут заказы отсортированы по стране
        self.assertEqual(valid_orders[0].__str__(), '87459;Молоко x2, Яблоки x2, Хлеб x1;Иванов Иван Иванович;Россия. Московская '
 'область. Москва. улица Пушкина;+7-912-345-67-89;MAX\n')
        self.assertEqual(valid_orders[1].__str__(), ('56342;Хлеб x2, Молоко x2;Смирнова Мария Леонидовна;Германия. Бавария. '
 'Мюнхен. Мариенплац;+4-989-234-56;LOW\n'))


if __name__ == '__main__':
    unittest.main()
