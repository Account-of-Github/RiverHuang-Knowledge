
import re

out_file = open('out.txt', 'w',encoding='UTF-8')

with open('黄河概览-python.txt', 'r',encoding='UTF-8') as f:
    for line in f:
        if(re.match('·[0-9].·', line)):
            print(line)
            continue
        sentences = line.strip().split('。')
        last_s = sentences[-1]
        sentences.pop()
        for s in sentences:
            out_file.write(s + '。\n')
        out_file.write(last_s)
out_file.close()