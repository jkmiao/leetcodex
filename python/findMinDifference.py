#!/usr/bin/env python
# coding=utf-8

"""
题目描述：
LeetCode 539. Minimum Time Difference

Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.

Example 1:

    Input: ["23:59","00:00"]
    Output: 1
    Note:

        The number of time points in the given list is at least 2 and won't exceed 20000.
        The input time is legal and ranges from 00:00 to 23:59.
        题目大意：
        给定一组24小时制的时间，格式为“小时：分钟”，求任意两组时间中分钟数间隔的最小值。

        注意：

        给定时间至少2个，至多20000个。
        给定时间是合法的，范围在00:00到23:59之间。
        解题思路：
        排序（Sort）

        将时间从小到大排序，然后将最小的时间小时+24后加入数组末尾。

        两两做差，求最小值即可。
"""


class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints
        :rtype: int
        """
        tp = sorted(map(int, p.split(':')) for p in timePoints)
        tp += [[tp[0][0]+24, tp[0][1]]]
        return min((tp[x+1][0]-tp[x][0])*60 + tp[x+1][1]-tp[x][1] for x in range(len(tp)-1))
