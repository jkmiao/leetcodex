#!/usr/bin/env python
# coding=utf-8

import argparse

class Solution(object):

    def trap1(self, A):
        """
        :type A: List{int}
        :rtype int  最大存储水量
        """

        leftmosthigh = [0 for i in range(len(A))]
        leftmax = 0

        for i in range(len(A)):
            leftmax = max(leftmax, A[i])
            leftmosthigh[i] = leftmax

        res = 0
        rightmax = 0
        for i in reversed(range(len(A))):
            rightmax = max(A[i], rightmax)
            if min(rightmax, leftmosthigh[i]) > A[i]:
                res += min(rightmax, leftmosthigh[i]) - A[i]
        return res


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('nums', nargs='+', type=int, help=' water bar high')
    args = parser.parse_args()

    test = Solution()
    print test.trap1(args.nums)
