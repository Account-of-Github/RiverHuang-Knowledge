#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import urllib.request
import urllib.parse
import json
import hashlib
import base64
'''
这是讯飞平台依存句法分析的demo
可以在平台的api文档中下载

1.以下三点需要替换为自己需要的
2.执行程序，报错信息中找到自己的ip
3.将ip添加到白名单中
4.等待一段时间后，再次执行即可

'''
#接口地址
url ="http://ltpapi.xfyun.cn/v1/cws"
#开放平台应用ID
x_appid = "*****"
#开放平台应用接口秘钥
api_key = "*******"
#语言文本
TEXT="汉皇重色思倾国，御宇多年求不得。杨家有女初长成，养在深闺人未识。天生丽质难自弃，一朝选在君王侧。"


def main():
    body = urllib.parse.urlencode({'text': TEXT}).encode('utf-8')
    param = {"type": "dependent"}
    x_param = base64.b64encode(json.dumps(param).replace(' ', '').encode('utf-8'))
    x_time = str(int(time.time()))
    x_checksum = hashlib.md5(api_key.encode('utf-8') + str(x_time).encode('utf-8') + x_param).hexdigest()
    x_header = {'X-Appid': x_appid,
                'X-CurTime': x_time,
                'X-Param': x_param,
                'X-CheckSum': x_checksum}
    req = urllib.request.Request(url, body, x_header)
    result = urllib.request.urlopen(req)
    result = result.read()
    print(result.decode('utf-8'))
    return


if __name__ == '__main__':
    main()
