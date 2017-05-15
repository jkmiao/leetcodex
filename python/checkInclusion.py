#!/usr/bin/env python
# coding=utf-8

from collections import Counter

class Solution(object):

    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l1, l2 = len(s1), len(s2)
        c1 = Counter(s1)
        c2 = Counter()
        p = q = 0
        while q < l2:
            c2[s2[q]] += 1
            if c1 == c2:
                return True
            q += 1
            if q - p + 1 > l1:
                c2[s2[p]] -= 1
                if c2[s2[p]] == 0:
                    del c2[s2[p]]
                p += 1
        return False

    def checkInclusion2(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l1, l2 = len(s1), len(s2)
        c1 = Counter(s1)
        c2 = Counter()
        cnt = 0
        p = q = 0
        while q < l2:
            c2[s2[q]] += 1
            if c1[s2[q]] == c2[s2[q]]:
                cnt += 1
            if cnt == len(c1):
                return True
            q += 1
            if q - p + 1 > l1:
                if c1[s2[p]] == c2[s2[p]]:
                    cnt -=1
                c2[s2[p]] -= 1
                if c2[s2[p]] == 0:
                    del c2[s2[p]]
                p += 1
        return False
