#!/usr/bin/env python
# encoding: utf-8

__author__ = 'Kane'

from multiprocessing import Process, Queue
import os, random, time

def write(q):
    for val in ['A', 'B', 'C']:
        print 'Put %s to queue...' % val
        q.put(val)
        time.sleep(random.random())

def read(q):
    while True:
        val = q.get(True)
        print 'Get %s from queue.' % val

if __name__ == '__main__':
    # 父进程创建 Queue, 并传给各个子进程
    q = Queue()

    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    # 启动子进程 pw, 写入:
    pw.start()
    # 启动子进程 pr, 读取:
    pr.start()

    # 等待 pw 结束
    pw.join()
    # pr 进程里是死循环，无法等待其结束，只能强行终止
    pr.terminate()
