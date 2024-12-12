"""
Заказы крупного онлайн-магазина
"""

import re
import os


class Order:
    """Класс содержит атрибуты заказа и методы для валидации и форматирования продуктов"""

    def __init__(self, order_id, products, customer_name, delivery_address, phone_number, delivery_priority):
        self.order_id = order_id
        self.products = products
        self.customer_name = customer_name
        self.delivery_address = delivery_address
        self.phone_number = phone_number
        self.delivery_priority = delivery_priority

    def validate(self) -> list:
        """
        Проверяет корректность заполнения адреса доставки и номера телефона по шаблону
        - Адрес: <Страна>. <Регион>. <Город>. <Улица>
        - Телефон: +x-xxx-xxx-xx-xx
        Возвращает список ошибок."""
        errors = []
        # Валидация адреса
        if not self.delivery_address:
            errors.append((1, "no data"))
        else:
            address_parts = self.delivery_address.split('.')
            if len(address_parts) != 4:
                errors.append((1, self.delivery_address))

        # Валидация номера
        phone_pattern = r'\+\d-\d{3}-\d{3}-\d{2}-\d{2}'
        if self.phone_number and not re.match(phone_pattern, self.phone_number):
            errors.append((2, self.phone_number))

        return errors

    def formatted_products(self) -> str:
        """Форматирует список продуктов в нужный вид с учетом количества"""
        product_count = {}
        for product in self.products.split(', '):
            product_count[product] = product_count.get(product, 0) + 1
        return ', '.join(f"{name} x{count}" for name, count in product_count.items())


class Utils:

    def __init__(self, orders_file_path:str, validate_orders_file_path:str, non_validate_file_path:str):
        self.abs_files_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "txtfiles")
        self.orders_file_path = os.path.join(self.abs_files_path, orders_file_path)
        self.validate_orders_file_path = os.path.join(self.abs_files_path, validate_orders_file_path)
        self.non_validate_file_path = os.path.join(self.abs_files_path, non_validate_file_path)

    def read_orders(self) -> list:
        """
        Считывает заказы из файла orders.txt и создает экземпляры класса Order
         - Принимает путь на файл с заказами
         - Возвращает список заказов
        """
        orders = []
        with open(self.orders_file_path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(';')
                if len(parts) != 6:
                    continue
                order = Order(
                    order_id=parts[0],
                    products=parts[1],
                    customer_name=parts[2],
                    delivery_address=parts[3],
                    phone_number=parts[4],
                    delivery_priority=parts[5]
                )
                orders.append(order)
        return orders

    def write_non_valid_orders(self, orders):
        """Записывает невалидные заказы в файл non_valid_orders"""
        with open(self.non_validate_file_path, 'w', encoding='utf-8') as file:
            for order in orders:
                errors = order.validate()
                for error_type, value in errors:
                    file.write(f"{order.order_id};{error_type};{value}\n")

    def write_valid_orders(self, orders):
        """
        Сортирует валидные заказы по стране, где первой всегда идёт Российская Федерация
        Остальные страны сортируются по алфавиту
        Внутри каждой страны сортировка по приоритету
        """
        valid_orders = [order for order in orders if not order.validate()]

        # Функция для сортировки по стране и приоритету
        def sort_key(order):
            country = order.delivery_address.split('.')[0]
            priority = {'MAX': 1, 'MIDDLE': 2, 'LOW': 3}[order.delivery_priority]

            if country == 'Российская Федерация' or "Ленинградская область" or "Московская область":
                return '', priority
            return country, priority

        # Сортируем по стране и приоритету
        valid_orders.sort(key=sort_key)

        with open(self.validate_orders_file_path, 'w', encoding='utf-8') as file:
            for order in valid_orders:
                address_parts = order.delivery_address.split('.')
                formatted_address = f"{address_parts[1].strip()}. {address_parts[2].strip()}. {address_parts[3].strip()}"
                file.write(
                    f"{order.order_id};{order.formatted_products()};{order.customer_name};{formatted_address};{order.phone_number};{order.delivery_priority}\n")


def main():
    utils = Utils("orders.txt","order_country.txt", "non_valid_orders.txt")
    orders = utils.read_orders()
    utils.write_non_valid_orders(orders)
    utils.write_valid_orders(orders)


if __name__ == "__main__":
    main()
