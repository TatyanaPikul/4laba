bilet=input("Введите номер билета ")
def f(bilet):
    if len(bilet) % 2 != 0:
       return False

    pol=len(bilet)//2
    ch1 = 0
    ch2 = 0

    for i in range(pol):
        ch1+=int(bilet[i])
        ch2+=int(bilet[i+pol])

    return ch1 == ch2

print(f(bilet))

