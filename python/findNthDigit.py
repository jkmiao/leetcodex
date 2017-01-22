#!/usr/bin/env python
# coding=utf-8

import argparse

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<10:
            return n
        len, cnt, start = 1, 9, 1
        while(n>len*cnt):
            n -= len * cnt
            len += 1
            cnt *= 10
            start *= 10
        start += (n-1)/len
        res = str(start)[(n-1)%len]
        return int(res)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int, help='Nth digit of num sequence')
    args = parser.parse_args()

    test = Solution()
    print test.findNthDigit(args.n)
