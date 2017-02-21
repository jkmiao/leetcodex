#!/usr/bin/env python
# coding=utf-8
"""
LeetCode 493. Reverse Pairs

Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3

"""

class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums2 = [n*2 for n in nums]
        dmap = {v:k+1 for k, v in enumerate(sorted(set(nums+nums2)))}
        ft = FenwickTree(len(dmap))
        ans = 0
        for n in nums2[::-1]:
            ans += ft.sum(dmap[n/2]-1)
            ft.add(dmap[n], 1)
        return ans


class FenwickTree(object):
    def __init__(self, n):
        self. n = n
        self.sums = [0] * (n+1)

    def add(self, x, val):
        while x<=self.n:
            self.sums[x] += val
            x += self.lowbit(x)

    def lowbit(self, x):
        return x & -x

    def sum(self, x):
        res = 0
        while x>0:
            res += self.sums[x]
            x -= self.lowbit(x)
        return res
