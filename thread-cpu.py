#!/usr/bin/env python
# encoding: utf-8

__author__ = 'Kane'

import threading, multiprocessing

# 运行并查看活动监视器中 cpu 占用比例
def loop():
    x = 0
    while True:
        x = x ^ 1

if __name__ == '__main__':
    for i in range(multiprocessing.cpu_count()):
        t = threading.Thread(target=loop)
        t.start()
