import re
import codecs
import time


def convertor(f):

    diction = {}
    result = ''

    result+='<?xml version="1.0" ?>'+'\n'

    result+='<Schedule>'+'\n'
    for i in f:
        KEY = re.compile(r'(?<=\")[-\w]+(?=\":)')
        VALUE = re.compile(r'(?<=:).*')
        tab = len(i)-len(i.lstrip())
        
        if re.search(r':\s\[\S+', i):
            key = KEY.search(i).group()
            value = VALUE.search(i).group()
            result+=(tab*' '+f'<{key}>'+'\n')

            for elem in re.findall(r'(?<=\s|\[)\S+(?=,|\])', value):
                elem = elem.replace('[','').replace(']','')
                result+=(tab+4)*' '+f'<item>{elem}</item>'+'\n'
            result+=(tab*' '+f'</{key}>'+'\n')
        elif re.search(r':.*?\{|\[', i):

            result+=(tab*' '+f'<{KEY.search(i).group()}>'+'\n')
            diction[tab] = f'</{KEY.search(i).group()}>'
        elif re.search(r'".*', i):

            key = KEY.search(i).group()
            value = VALUE.search(i).group()
            if value[-1]==',': value = value[:-1]
            value = value.replace('"','')
            result+=(tab*' '+f'<{key}>{value[1:]}</{key}>'+'\n')

        elif tab in diction.keys():

            result+=(tab*' '+diction[tab]+'\n')

        elif re.search(r'(?!<=")\S+(?!=")', i):
            result+=re.sub(r'\S+', lambda x:"<item>"+x.group().replace(',', '')+"</item>",i)

    result+='</Schedule>'+'\n'
    result = re.sub(r'>\s(?=("|\[))', r'>', result)
    return result

if __name__ == '__main__':

    with open("schedule.json", encoding='utf-8') as w:
        f = w.readlines()[1:-1]
    start_time = time.time()
    
    result = convertor(f)
    print("--- %s seconds ---" % (time.time() - start_time))
   
    with codecs.open('third_task.xml', 'w', "utf-8") as file:
        file.write(result)

