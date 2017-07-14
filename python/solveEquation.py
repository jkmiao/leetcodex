#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2017/07/09/leetcode-solve-the-equation/

题目大意：
    给定一元一次方程，求x的值

解题思路：
    字符串处理

    用'='将等式分为左右两半
    分别求左右两侧x的系数和常数值，记为lx, lc, rx, rc
    令x, c = lx - rx, rc - lc
    若x != 0，则x = c / x
    否则，若c != 0，说明方程无解
    否则，说明有无数组解

"""

class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        left, right = equation.split('=')
        lx, lc = self.solve(left)
        rx, rc = self.solve(right)
        x, c = lx - rx, rc-lc
        if x:
            return 'x=%d' %(c/x)
        elif c:
            return 'No solution'
        return 'Infinite solutions'

    def solve(self, expr):
        x = c = 0
        num, sig = '', 1
        for ch in expr + '#':
            if '0' <= ch <= '9':
                num += ch
            elif ch == 'x':
                x += int(num or '1') * sig
                num, sig = '', 1
            else:
                c += int(num or '0') * sig
                num, sig = '', 1
                if ch=='-':
                    sig = -1
        return x, c



if __name__ == '__main__':

    test = Solution()
    expr = "2x+3x-6x=x+2"
    print test.solveEquation(expr)
