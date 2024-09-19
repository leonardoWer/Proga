# print(eval(input("Введите математическое выражение: ")))
num1,num2,symvol = 0,0,""
num1, num2 = map(int, input("Введите первое и второе число: ").split())
symvol = str(input("Введите математический символ: "))

def calc(num1,num2, symvol):
    res = 0
    if symvol=="+":
        res = num1+num2
    if symvol=="-":
        res = num1-num2
    if symvol=="/":
        res = num1/num2
    if symvol=="*":
        res = num1*num2
    else:
        return "Ошибка чтения выражения"
    return res

print(calc(num1, num2, symvol))
