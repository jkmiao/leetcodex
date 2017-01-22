#!/usr/bin/env python
# coding=utf-8

"""
11. Container With Most Water   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 110418
Total Submissions: 306322
Difficulty: Medium
Contributors: Admin
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""

class Solution(object):

    def maxArea(self, height):
        """
        :type height: List(int)
        :rtype: int
        """
        ans = 0
        if len(height)<2:
            return ans
        left, right = 0, len(height)-1

        while(left<right):
            volume = (right-left) * min(height[left], height[right])
            ans = max(ans, volume)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans


if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('height', type=int, nargs='+')
    args = parser.parse_args()
    print(args.height)
    test = Solution()
    print test.maxArea(args.height)
