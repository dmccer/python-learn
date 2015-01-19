#!/usr/bin/env python
# encoding: utf-8

__author__ = 'Kane'

from pyquery import PyQuery as pq
import urllib2
import json
import codecs

root_url = 'http://www.cnsat.net/'

def parse_cnsat(doc):
    td = doc('table').eq(2).find('tr td').not_('[colspan="2"]').not_('[rowspan="35"]')

    # 无法处理的数据
    # td110 = td.eq(110)

    td = td[:110] + td[111:]

    sat_list = []
    i, n = 0, len(td)

    while i < n:
        d = dict()
        t = pq(td[i]).text().strip().replace(r"\r\n", '').split()
        t = [' '.join(t[:-1])] + t[-1:]
        l = len(t)

        d['index'] = i
        if l:
            d['sat_name'] = t[0];
            if l > 1:
                d['sat_deg'] = t[1];
            d['update_date'] = pq(td[i+1]).text()

        sat_list.append(d)
        i = i + 2

    with codecs.open('/Users/kane/sat', 'w', 'utf-8') as f:
        f.write(json.dumps(sat_list, encoding="UTF-8", ensure_ascii=False))

def crawl(root_url):
    res = urllib2.urlopen(root_url)
    html = res.read()

    doc = pq(html)
    parse_cnsat(doc)

if __name__ == '__main__':
    crawl(root_url)

