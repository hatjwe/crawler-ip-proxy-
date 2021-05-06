import time

import requests
from lxml import etree


def get_url():
    for i in range(1, 9):
        # get_url(i)
        url = "http://www.89ip.cn/index_" + str(i) + ".html"
        html = requests.get(url).text

        html = etree.HTML(html)
        result = html.xpath('//td[2]/text()')
        result2 = html.xpath('//td[1]/text()')
        for a, b in zip(result2, result):
            # PORT = b.replace(" ", "")
            # IP = a.replace(" ", "")
            PORT = b.lstrip()
            PORT = PORT.rstrip()
            IP = a.rstrip()
            IP = IP.lstrip()
            DL = (IP + ':' + PORT)
            with open('DL1.txt', 'a') as f:
                f.write(DL + "\n")
        time.sleep(3)
    print("爬取完毕！")


def check(DL):
    url = 'http://%s' % DL.rstrip()
    try:
        result = requests.get(url, timeout=5)
        print(DL + "可用")
        with open('可用的IP.txt', 'a') as f:
            f.write(DL + "\n")
    except:
        print(DL + '不可用')


if __name__ == '__main__':
    get_url()
    with open("DL1.txt", 'r') as F:
        Str = F.readlines()
        for i in Str:
            check(i)
