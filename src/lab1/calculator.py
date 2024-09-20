"""
Содержит функции:
-Главная функция
-Функция калькулятор
"""

def main():
    """
    Определяет переменные и математическую операцию\n
    Далее вызывает функцию калькулятор
    Возвращает результат
    """
    num1, num2 = map(int, input("Введите первое и второе число: ").split())
    symvol = str(input("Введите математический символ: "))
    print(calc(num1, num2, symvol))

def calc(num1,num2, symvol):
    """
    Принимает две цифры и математический символ
    - Выполняет операции сложения, вычитания, умножения, деления
    """
    res = 0
    if symvol=="+":
        res = num1+num2
    elif symvol=="-":
        res = num1-num2
    elif symvol=="/":
        if num2 !=0:
            res = num1/num2
        else:
            return "На ноль делить нельзя!"
    elif symvol=="*":
        res = num1*num2
    else:
        return "Ошибка чтения выражения"
    return res

main()
