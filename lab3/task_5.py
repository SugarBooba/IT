import codecs


def tag_sorter(s, tag):
    if isinstance(s[tag], list):
        return 1
    elif isinstance(s[tag], dict):
        return 2

    return 0


def jsonToXml(s, result='', tag=''):
    tag2 = tag
    result = ''

    if type(s) is dict:
        for tag in sorted(s, key=lambda tag: tag_sorter(s, tag)):
            if f"'{tag}':"+' {' in str(s):
                if len(tag2) > 1:

                    result += f"[{tag2[1:]}.{tag}]\n" + \
                        jsonToXml(s[tag], result, tag2+'.'+tag)+'\n'
                else:
                    result += f"[{tag}]\n" + \
                        jsonToXml(s[tag], result, tag2+'.'+tag)+'\n'

            else:

                result += f"{tag} = " + jsonToXml(s[tag], result, tag2)

    elif type(s) is list:
        result += f'{s}'+'\n'

    else:
        result += f'"{s}"\n'

    return result


if __name__ == '__main__':
    with open("schedule.json", encoding='utf-8') as w:
        f = w.read()
    xml_text = jsonToXml(eval(f))
    with codecs.open('fifth_task.toml', 'w', "utf-8") as f:
        f.write(xml_text)
