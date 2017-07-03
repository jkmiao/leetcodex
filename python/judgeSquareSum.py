#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2017/07/02/leetcode-sum-of-square-numbers/

大意: 给定非负整数c, 判断是否存在两个整数a和b, 满足 a^2 + b^2 = c.
思路: 在范围[0, int(sqrt(c))]内枚举a, 判断c-a^2是否为完全平方数.

"""


class Solution(object):

    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for a in range(int(c**0.5)+1):
            b2 = c - a ** 2
            if (int(b2**0.5)) ** 2 == b2:
                return True
        return False
