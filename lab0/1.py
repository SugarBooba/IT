

def convertor(b,c,d):
  let = {"10":"A", "11":"B", "12":"B", "13":"D", "14":"E", "15":"F"}
  a = ""
  b = int(str(b),d)
  while b>0:
    if str(b%c) in let:
      a = let[str(b%c)]+ a
    else:
      a=str(b%c) + a
    b//=c
  return a

def fac(b):
  a = ""
  l = 2
  while b>0:
    a = str(b%l)+a
    b //=l
    l+=1
  return a

b = int(input("Введите число, корторое нужно перевести: "))
d = int(input('Введите систему счисления числа: '))
c = int(input("Введите систему счисления, в которую нужно перевести число (0 если факториальная): "))
if c == 0:
  print(fac(b))
else:
  print(convertor(b,c,d))