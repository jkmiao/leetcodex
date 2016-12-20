#!/usr/bin/env python
# coding=utf-8

import argparse

class Solution(object):

    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 0
        elif n%2==0:
            return self.integerReplacement(n/2) + 1
        else:
            return min(self.integerReplacement(n-1), self.integerReplacement(n+1))+1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=int)
    args = parser.parse_args()
    test = Solution()
    print test.integerReplacement(args.n)

       

