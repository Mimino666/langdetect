#!/usr/bin/env python
# coding:utf-8
# Author: veelion@ebuinfo.com
'''
remove Chinese charactors from profiles/ko,
to make sure Chinese is not mistakenly be detected as Korean
'''

import json


def is_zh(txt):
    for u in txt:
        ui = ord(u)
        if 0x4E00 <= ui <= 0x9FCF:
            return True
    return False


def remove_zh(d):
    nd = {}
    for k, v in d.items():
        txt = k.strip()
        if is_zh(txt):
            print 'chinese:', txt
            continue
        nd[k.encode('utf8')] = v
    return nd


def fix(fn):
    jn = json.load(open(fn))
    ndata = {}
    for k,v in jn.items():
        if k == 'freq':
            nv = remove_zh(v)
            ndata[k] = nv
        else:
            ndata[k] = v
    fo = open(fn, 'w')
    json.dump(ndata, fo, ensure_ascii=False)


if __name__ == '__main__':
    fix('profiles/ko')

