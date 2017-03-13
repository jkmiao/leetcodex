#!/usr/bin/env python
# coding=utf-8

import math

"""
题目描述：
LeetCode 541. Reverse String II

Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.

Example:

    Input: s = "abcdefg", k = 2
    Output: "bacdfeg"

"""

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ''
        round = int(math.ceil(len(s)/(2.0 * k)))
        for x in range(round):
            res += s[x*2*k:(x*2+1)*k][::-1]
            res += s[(x*2+1)*k:(x*2+2)*k]
        return res
