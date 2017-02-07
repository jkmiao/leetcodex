#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        now = ans = 0
        for st in timeSeries:
            ans += min(duration, st+duration-now)
            now = st + duration
        return ans
