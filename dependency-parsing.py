#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import urllib.request
import urllib.parse
import json
import hashlib
import base64
'''
依存句法分析
'''
#接口地址
baseUrl = "http://ltpapi.xfyun.cn/v1"
#角色语义标注
cwsUrl = baseUrl + "/cws"
#依存句法分析
dpUrl = baseUrl + "/dp"
#语义依存分析（树）
sdpUrl = baseUrl + "/sdp"
#测试用url
url ="http://ltpapi.xfyun.cn/v1/dp"
#开放平台应用ID
x_appid = "602c90ad"
#开放平台应用接口秘钥
api_key = "0ee183865fc62d36802967253e1877cf"
#语言文本
TEXT = "黄河概览［地形地貌】 黄河是我国的第二大河．发源千青藏高原巴颜喀拉山北麓海拔 4500m的约古宗列盆地，流经青海、四川、甘肃、宁夏、内蒙古、山西 、陕西、河南、山东等9省（区），在山东省垦利区注入渤海。"

#分析一个句子
def analyse(sentence):
    body = urllib.parse.urlencode({'text': sentence}).encode('utf-8')
    param = {"type": "dependent"}
    x_param = base64.b64encode(json.dumps(param).replace(' ', '').encode('utf-8'))
    x_time = str(int(time.time()))
    x_checksum = hashlib.md5(api_key.encode('utf-8') + str(x_time).encode('utf-8') + x_param).hexdigest()
    x_header = {'X-Appid': x_appid,
                'X-CurTime': x_time,
                'X-Param': x_param,
                'X-CheckSum': x_checksum}

    cwsReq = urllib.request.Request(cwsUrl, body, x_header)
    cwsResult = urllib.request.urlopen(cwsReq)
    cwsResult = cwsResult.read()

    data = json.loads(cwsResult.decode('utf-8'))['data']
    word = data['word']

    dpReq = urllib.request.Request(dpUrl, body, x_header)
    dpResult = urllib.request.urlopen(dpReq)
    dpResult = dpResult.read()

    data = json.loads(dpResult.decode('utf-8'))['data']
    dp = data['dp']

    sdpReq = urllib.request.Request(sdpUrl, body, x_header)
    sdpResult = urllib.request.urlopen(sdpReq)
    sdpResult = sdpResult.read()

    data = json.loads(sdpResult.decode('utf-8'))['data']
    sdp = data['sdp']

    print(word)
    print(dp)
    # print(sdp)
    #返回值修改为需要的格式
    rs = {
        'word': word,
        'dp': dp,
        'sdp': sdp
    }

    return rs


def main():
    analyse(TEXT)
    #处理并输出到文件中
    # out_file =  out_file = open('out-2.txt', 'w',encoding='UTF-8')
    # with open('out.txt', 'r', encoding='UTF-8') as f:
    #     for line in f:
    #         d = analyse(line.strip())
    #         out_file.write(str(d) + "\n")
    #         #print(str(d))
    # return

if __name__ == '__main__':
    main()
