# 0
import re

s1 = "Перед вами трёхстишия, которые претендуют на то, чтобы быть хайку."
s2 = "В качестве разделителя строк / используются символы."
s3 = "Если разделить / то выведите привет / иначе пока"
s4 = "Если число строк не равно / выведите строку  / «Не хайку."
s5 = "Иначе и вы / пропускаете ходы / и все заново"
s6 = "Иначе и вы. пропускаете ходы / и все заново"

s = [s1, s2, s3, s4, s5, s6]


def sec_task(s):
# .!?;
    # Checking that line consists of 3 parts
    if re.fullmatch(r'.*?([.!?;/]).*?\1.*', s):
        # Splitting correct string for /
        s = re.split(r'[.!?;/]', s)
        # Checking that all parts make up correct values of syllables
        if len(re.findall(r'[уеыаоэёяиюУЕЫАОЭЁЯИЮ]{1}', s[0])) == 5 and len(re.findall(r'[уеыаоэёяиюУЕЫАОЭЁЯИЮ]{1}', s[1])) == 7 and len(re.findall(r'[уеыаоэёяиюУЕЫАОЭЁЯИЮ]{1}', s[2])) == 5:
            print('Хайку!')
        else:
            print("Не хайку.")
    # outputting that length of string is not correct 
    elif len(re.findall(r'/', s)) != 2:
        print('Не хайку. Должно быть 3 строки.')

# (.*?[уеыаоэёяиюУЕЫАОЭЁЯИЮ]){5}.*?/(.*?[уеыаоэёяиюУЕЫАОЭЁЯИЮ]){7}.*? / (.*?[уеыаоэёяиюУЕЫАОЭЁЯИЮ]){5}.*?
a = int(input('Write 1 if for your test: '))
if a == 1:
    s = input("Just write your line ")
    if re.search(r'[a-zA-Z]', s):
        print("Write the line on Russian")
    else:
        sec_task(s)
else:
    for i in s:
        sec_task(i)

# (re.fullmatch(r'[а-яА-Я ]*/[а-яА-Я ]*/[а-яА-Я ]*', s3))