a=int(input("Введите число "))

def f(a):
    if a==0:
        return "ZeroDivisionError"
    elif a<0:
        return "MinusError"
    else:
        r=100/a
        return r

print(f(a))