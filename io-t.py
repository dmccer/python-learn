#!/usr/bin/env python
# encoding: utf-8

__author__ = 'Kane'

import os
import sys

def search(s):
    if not os.path.exists(s):
        print '不存在目录 %s'

    for c in os.listdir(s):
        _c = os.path.join(s, c)

        if os.path.isdir(_c):
            search(_c)
        else:
            print _c

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print '请输入搜索的目录'
    elif len(sys.argv) == 2:
        search(sys.argv[1])
    else:
        raise
