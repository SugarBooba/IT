import re
s = 'Довольно    распространённая ошибка ошибка – это лишний повтор повтор слова слова. Смешно, не не правда ли? Не нужно портить хор хоровод'

# print(re.findall(r'\w*\b'))
s = re.sub(' +', ' ', s)

print(re.sub(r'(\w+)\W+(?=\1\b)', '', s))
    