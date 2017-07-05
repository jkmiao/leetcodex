#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2014/12/30/leetcode-factorial-trailing-zeroes/

大意: Given an integer n, return the number of trailing zeroes in n!.
solution:  考虑n!中5的质数因子个数

n!后缀0的个数 = n!质因子中5的个数 = floor(n/5) + floor(n/25) + floor(n/125)

"""

class Solution(object):

    def trailingZeroes(self, n):
        x = 5
        ans = 0
        while n >= x:
            ans += n/x
            x *= 5
        return ans
