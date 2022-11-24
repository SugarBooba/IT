

def convertor(b, c, d):
    let = {"10": "A", "11": "B", "12": "B", "13": "D", "14": "E", "15": "F"}
    a = ""
    b = int(str(b), d)
    while b > 0:
        if str(b % c) in let:
            a = let[str(b % c)] + a
        else:
            a = str(b % c) + a
        b //= c
    return a


def fac(b, d):
    a = ""
    l = 2
    b = int(str(b), d)
    while b > 0:
        a = str(b % l)+a
        b //= l
        l += 1
    return a


b = (input("Введите число, которое нужно перевести: "))
d = int(input('Введите систему счисления числа: '))
c = int(input("Введите систему счисления, в которую нужно перевести число (0 если факториальная): "))


def err(b, c):

    let = {"10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"}

    lis = []
    for i in range(c):
        if str(i).title() in let:
            lis.append(let[str(i)])
        else:
            lis.append(str(i))
    for i in str(b):
        if i.title() not in lis:
            print('Неверное число')
            # print(lis)
            return 0
            # break
    return 1


if err(b, d):
    if c == 0:
        print(fac(b, d))
    else:
        print(convertor(b, c, d))

