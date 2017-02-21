#!/usr/bin/env python
# coding=utf-8

import argparse

"""
Given a string, sort it in decreasing order based on the frequency of characters.
https://leetcode.com/problems/sort-characters-by-frequency/
"""

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        cnt = Counter(s)
        res = [k*v for (k, v) in cnt.most_common()]
        return ''.join(res)


if __name__ == "__main__":
    test = Solution()
    parser = argparse.ArgumentParser()
    parser.add_argument('s', type=str, help='input a string to be sort')
    args = parser.parse_args()
    print test.frequencySort(args.s)
