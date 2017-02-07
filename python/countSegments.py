#!/usr/bin/env python
# coding=utf-8


class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        segs = s.split()
        return segs


if __name__ == "__main__":

    test = Solution()
    print test.countSegments('fja    dfj l,df ad  ')
