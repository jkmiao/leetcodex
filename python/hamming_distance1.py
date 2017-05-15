#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2016/12/18/leetcode-hamming-distance/

题目大意：
两个整数的汉明距离是指其二进制不相等的位的个数。

给定两个整数x和y，计算汉明距离。

注意：

0 ≤ x, y < 2^31.

解题思路：
异或运算

"""

class Solution(object):

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype :int
        """
        return bin(x ^ y).count('1')



if __name__ == '__main__':
    test = Solution()
    print test.hammingDistance(1, 4)
