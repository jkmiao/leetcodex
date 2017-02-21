#!/usr/bin/env python
# coding=utf-8

import collections

class Solution(object):
    def detectCapitalUse(self, word):
        """

        :type word: str
        :rtype: bool
        """
        return word[1:].islower() or word.islower() or word.isupper()

    def findMaxLength(self, nums):
        """
        给定一个二进制数组，求其中满足0的个数与1的个数相等的最长子数组
        注意：给定二进制数组的长度不超过50,000
        :type nums: List[int]
        :rtype: int
        """
        sums = [0] * len(nums)
        dmap = collections.defaultdict(int)
        last = 0
        for i, n in enumerate(nums):
            last += 2*nums[i]-1
            sums[i] = last
            dmap[last] = max(dmap[last], i)
        ans = 0
        for i, m in enumerate(sums):
            if m == 0:
                ans = max(ans, i+1)
            else:
                ans = max(ans, dmap[m]-i)
        return ans
