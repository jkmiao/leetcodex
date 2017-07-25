#!/usr/bin/env python
# coding=utf-8


"""
题目描述：
LeetCode 645. Set Mismatch

The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:

    Input: nums = [1,2,2,4]
    Output: [2,3]
    Note:

    The given array size will in the range [2, 10000].
    The given array's numbers won't have any order.
    题目大意：
    集合S初始包含数字1到n。其中一个数字缺失，一个数字重复。

    求其中重复的数字，与缺失的数字。

http://bookshadow.com/weblog/2017/07/24/leetcode-set-mismatch/

"""

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :type: List[int]
        """
        s = set()
        m = len(nums)
        total = (1 + m)*m/2
        for n in nums:
            if n not in s:
                s.add(n)
            else:
                return [n, total+n-sum(nums)]


if __name__ == "__main__":

    test = Solution()
    nums = [1, 2, 3, 3]
    print test.findErrorNums(nums)
