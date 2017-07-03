#!/usr/bin/env python
# encoding=utf-8

"""
http://bookshadow.com/weblog/2017/05/21/leetcode-longest-harmonious-subsequence/

LeetCode 594. Longest Harmonious Subsequence

We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:

Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Note: The length of the input array will not exceed 20,000.

大意: 给定整数数组nums, 求其中最大值与最小值相差恰好为1的子序列长度的最大值

思路: 用字典cnt统计各数字出现的次数. 升序遍历cnt的键值对

"""

from collections import Counter

class Solution(object):
     def findHS(self, nums):
          """
          :type name: List[int]
          :rtype: int
          """
          cnt = Counter(nums)
          ans = 0
          lastKey = lastVal = None
          for key, val in sorted(cnt.items()):
              if lastKey is not None and lastKey + 1==key:
                  ans = max(ans, val + lastVal)
	      lastKey, lastVal = key, val
	  return ans


if __name__ == '__main__':
     test = Solution()
     a = [1, 3, 2, 2, 5, 2, 3, 7]
     print test.findHS(a)	
