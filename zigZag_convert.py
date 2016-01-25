#!/usr/bin/env python
# coding=utf-8
import sys

# https://leetcode.com/problems/zigzag-conversion/
def convert (s,numRows):
    if numRows<2:return s

    tmp = ['' for i in range(numRows)]
    index,step = -1,1
    for i in range(len(s)):
        index += step
        if index == numRows:
            index = numRows-2
            step =- 1
        elif index == -1:
            index = 1
            step = 1
        tmp[index]+=s[i]

    return ''.join(tmp)



s,n = sys.argv[1],int(sys.argv[2])

print convert(s,n)
