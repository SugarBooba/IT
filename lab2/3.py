# 2
import re

s1 = '20 + 22 = 42'
s2 = '22 + 323!!!4 = 2354678'
s3 = '- 23.45 - 3456 = 3456'
s4 = '231 - 353 = 46'
s5 = 'sin(234) + 3456 '

s = [s1, s2, s3, s4, s5]

def numb_convertor(i):
    # checking + or -
    if i.count('-')!=0 and re.search(r'- \b(?<![^0-9 ])\d+(?![^0-9 ])\b', i):
        
        i = re.sub(r'- \b(?<![^0-9 ])\d+(?![^0-9 ])\b', lambda x: ("+ "+ x.group()[2:]), i)

    print(re.sub(r'\b(?<![^0-9 ])\d+(?![^0-9 ])\b', lambda x: str(4*int(x.group())**2-7), i))

a = int(input('Write 1 if for your test: '))
if a == 1:
    numb_convertor(input("Just write your line "))
else:

    for i in s:
        numb_convertor(i)
