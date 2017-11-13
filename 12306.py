# -*- coding:utf-8 -*-
import urllib.request,nturl2path,macurl2path
import ssl
import json

#关闭ssl认证
ssl._create_default_https_context=ssl._create_unverified_context

def pew(number):
    if number == 26:
        return '无座'
    elif number == 29:
        return '硬座'
    elif number == 28:
        return '硬卧'
    elif number == 23:
        return '软卧'
    elif number == 29:
        return '软卧'
    elif number == 30:
        return '二等座'
    elif number == 31:
        return '一等座'
    elif number == 32:
        return '商务特等座'
    else:
        return ''


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-11-20&leftTicketDTO.from_station=HZH&leftTicketDTO.to_station=LZJ&purpose_codes=ADULT'

def getTicketLit():
    #获取请求地址内容
    req = urllib.request.Request(url)
    req.headers = headers
    res=urllib.request.urlopen(req)
    html=res.read()
    #输出
    result = json.loads(html);
    result2 = result['data']['result'];
    m = 0
    for i in result2:
        m += 1
        tmp_list = i.split('|')
        #判断是哪个班次
        if tmp_list[3] != 'K308':
            break
        print('班次是：' + tmp_list[3])
        #print(tmp_list)
        # a：3-哪一班车
        # a: 26-无座，29-硬座， -软座，  28-硬卧， -动卧，23-软卧， 高级软卧,30-二等座，31-一等座，32-商务特等座
        a = 0
        for n in tmp_list:

            #针对硬卧开始判断
            if a==28:
                #print('[a=%s] %s：%s' % (a, pew(a), n))
                if n=='有' or is_number(n) :print( tmp_list[3]+'的'+pew(a)+'票数：'+n)
                else: print( tmp_list[3]+'的'+pew(a)+'票数：'+'没票')
            a += 1






getTicketLit()