a=int(input("Введите число в формате ДД "))
b=int(input("Введите месяц в формате ММ "))
c=int(input("Введите год в формате ГГГГ "))

def f(a,b,c):
    kon=c%100
    if a*b==kon:
        return True
    else:
        return False
print(f(a,b,c))