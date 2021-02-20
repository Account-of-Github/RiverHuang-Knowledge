
import re
'''
预处理
'''
out_file = open('out.txt', 'w',encoding='UTF-8')

with open('黄河概览-python.txt', 'r',encoding='UTF-8') as f:
    for line in f:
        #删去所有的标题
        if(re.match('·[0-9].·', line)):
            print(line)
            continue
        #取每个句号为一行
        sentences = line.strip().split('。')
        last_s = sentences[-1]
        sentences.pop()
        for s in sentences:
            out_file.write(s + '。\n')
        out_file.write(last_s)
out_file.close()