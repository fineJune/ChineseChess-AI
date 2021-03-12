# -*-coding:utf-8-*-

"""
@author cc
@date 2021/3/6
"""

import requests
import re
from urllib.request import urlretrieve
import time
from lxml import etree
import os

def getList():
    url='http://www.zgxqds.com/xqpk_list.asp?page={page}&bigclass=&midclass=&smallclass=&namekey=&xq_red=&xq_black=&qishou=&sortStr=&radiobutton=&xq_date='
    with open('moveSet.txt','w',encoding='utf-8') as fp:
        for page in range(1299):
            resp=requests.get(url.format(page=page))
            for l in etree.HTML(resp.text).xpath("//tr[@align='center']"):
                try:
                    url1='http://www.zgxqds.com/'+l.xpath(".//td//a")[0].get('href')
                except:
                    continue
                else:
                    try:
                        resp1=requests.get(url1)
                        moveSet=re.search('XQ_movelist\](\d*?)\[',resp1.text).group(1)
                    except:
                        pass
                    else:
                        fp.write(moveSet+'\n')


def loadBook():
    with open('book.txt','w',encoding='utf-8') as fp:
        for book in os.listdir('./src/book'):
            if 'pgn' in book:
                content=open(book,'r',encoding='GBK').readlines()
                moveSet=''
                for line in content:
                    if not line.startswith('['):
                        redMove,blackMove=line.split(' ')[-2:]








getList()

