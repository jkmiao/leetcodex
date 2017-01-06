#!/usr/bin/env python
# coding=utf-8

import argparse

"""
423. Reconstruct Original Digits from English   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 5657
Total Submissions: 13409
Difficulty: Medium
Contributors: Admin
Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
    Input contains only lowercase English letters.
    Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
    Input length is less than 50,000.
    Example 1:
        Input: "owoztneoer"

        Output: "012"
    
    Example 2:
        Input: "fviefuro"
        Output: "45"


"""

import collections

class Solution(object):

    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """

        cnts = collections.Counter(s)
        nums = ['six', 'zero', 'two', 'eight', 'seven', 'four', 'five', 'nine', 'one', 'three']
        numc = [collections.Counter(num) for num in nums]
        digits = [6, 0, 2, 8, 7, 4, 5, 9, 1, 3]
        ans = [0]*10
        for idx, num in enumerate(nums):
            cntn = numc[idx]
            t = min(cnts[c]/cntn[c] for c in cntn)
            ans[digits[idx]] = t
            for c in cntn:
                cnts[c] -= t * cntn[c]

        return ''.join(str(i) * n for i, n in enumerate(ans))




if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('s', help='input string', type=str)
    args = parser.parse_args()

    test = Solution()
    print test.originalDigits(args.s)

