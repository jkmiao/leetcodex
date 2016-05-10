#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

    """
    def maxProfit(self,prices):
        n = len(prices)
        if n<2:
            return 0
        sells = [None]*n
        buys = [None]*n
        sells[0],buys[0] = 0,-prices[0]
        for i in range(1,n):
            delta = prices[i]-prices[i-1]
            sells[i] = max(buys[i-1]+prices[i],sells[i-1]+delta)
            buys[i] = max(sells[i-2]-prices[i] if i>1 else None,buys[i-1]-delta)
        return max(sells)
