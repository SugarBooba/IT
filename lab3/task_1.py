import time
import codecs


def wrapper(f):

    result = ''
    result += '<?xml version="1.0" ?>\n'
    result += '<Schedule>\n'
    result += jsonToXml(f, padding='\t')
    result += '</Schedule>\n'

    return result


def jsonToXml(s, result='', padding=''):

    result = ''

    if type(s) is dict:

        for tag in sorted(s, key=lambda key: not isinstance(key, (list, dict))):

            result += f"{padding}<{tag}>\n" + \
                jsonToXml(s[tag], result, "\t" + padding) + \
                f"{padding}</{tag}>\n"

    elif type(s) is list:
        for i in s:

            result += f"{padding}<item>{i}</item>\n"

    else:
        result += f"{padding}{s}\n"

    return result


if __name__ == '__main__':
    with open("schedule.json", encoding='utf-8') as w:
        f = w.read()

    start_time = time.time()

    xml_text = wrapper(eval(f))

    print("--- %s seconds --" % (time.time() - start_time))

    with codecs.open('first_task.xml', 'w', "utf-8") as f:
        f.write(xml_text)

    print(xml_text)
