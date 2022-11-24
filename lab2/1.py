# :-{/ 025
import re

s1 = ":-{/:-{/efjenfiebfeibuu/-{/efjenfiebfeibuu:-{/feuwdub"
s2 = "fce:-{/eifne:-{/efinofefiefibebo:-{/efwbwds3:-{/"
s3 = ":-{/:-{/:-{/edfetf:{:-{/efeiufoqa"
s4 = "fne:-{/efinofefiefibebo:-{/:-{/efj"
s5 ="ce:-{/eifbo:-{/:-{/ef:-{/{/feyfb0\8as7:-{/:-{wfwfwef/))%-)%-)"

s = [s1, s2, s3, s4, s5]
def find_smile(s, a=':-{/' ):
    print(len(a.findall(s)), end=' ')

a = int(input('Write 1 if for your test: '))
if a == 1:
    find = (input("Just write your smile "))
    find = re.escape(find)
    find = re.compile(find)
    for i in s:
        find_smile(i, a=(find))
else:

    for i in s:
        find_smile(i)


# def checker(f):
#     if re.findall(r'[(){}+.?*]', f):
#         return re.sub(r'[)}]+.?*]', lambda x: ("\""+x.group()), f)
# import re

# s = checker(input())
# print(s)
# s = re.compile(input())
# print(s.findall('123356123'))