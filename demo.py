# -*- coding:utf-8 -*-


import json
import ssl
import urllib.request
import cons
import requests

DATE = '2018-06-18'
TO_STATION = 'AOH'
FROM_STATION = 'WHN'

# ssl._create_default_https_context = ssl._create_unverified_context

def getlist(train_date, from_station, to_station):
    # req = urllib.request.Request(
    #     'https://kyfw.12306.cn/otn/leftTicket/queryO?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT' % (
    #         train_date, from_station, to_station))
    req = requests.get(
        'https://kyfw.12306.cn/otn/leftTicket/queryO?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT' % (
            train_date, from_station, to_station))
    # req.add_header('User-Agent',
    #                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36')
    # html = urllib.request.urlopen(req).read()
    # html = html.decode('utf-8-sig')
    html = req.text
    print(html)
    # dict = json.loads(html)
    # result = dict['data']['result']
    # for i in result:
    #     if i:
    #         n = i.split('|')
    #         train = n[3]
    #         shangwuzuo = n[32]
    #         yidengzuo = n[31]
    #         erdengzuo = n[30]
    #         ruanwo = n[23]
    #         yingwo = n[28]
    #         yingzuo = n[29]
    #         wuzuo = n[26]
    #         print('车次:%s，商务座:%s一等座:%s，二等座:%s,软卧:%s，硬卧:%s，硬座:%s，无座:%s' % (
    #             train, shangwuzuo, yidengzuo, erdengzuo, ruanwo, yingwo, yingzuo, wuzuo,))
    # return result


def stations_name(name):
    stations = {}
    for i in cons.station_names.split('@'):
        if i:
            n = i.split('|')
            stations[n[1]] = n[2]
    station = stations[name]
    return station


def main():
    # train_date = input('请输入时间 如2018-01-04')
    # from_station = input('出发站')
    # to_station = input('终点站')
    getlist(DATE, FROM_STATION, TO_STATION)


if __name__ == '__main__':
    main()
