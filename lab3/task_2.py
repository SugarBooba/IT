import json
from json2xml import json2xml
import time
import codecs


def convertor(f):
    jess_dict = (json.loads(f))
    result = json2xml.Json2xml(jess_dict, attr_type=False).to_xml()
    
    return result

if __name__ == '__main__':

    with open("schedule.json", encoding='utf-8') as w:
        f = w.read()
    start_time = time.time()

    result = convertor(f)
    print("--- %s seconds ---" % (time.time() - start_time))
    file =  codecs.open('second_task.xml', 'w', 'utf-8')
    file.write(result)
    file.close()