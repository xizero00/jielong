import os
filename = r'C:\Users\dx\Desktop\名单.txt'

names, ids = [], []
with open(filename, 'r', encoding='utf-16') as fd:
    for line in fd:
        line = line.strip()
        if len(line) > 0:
            name, id = line.split('\t')
            names.append(name)
            ids.append(id)


with open(r'C:\Users\dx\Desktop\list.txt', 'w') as fd:
    for i in range(len(names)):
        fd.write('{}&{},'.format(names[i], ids[i]))




