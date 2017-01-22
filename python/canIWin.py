#!/usr/bin/env python
# coding=utf-8

import argparse

"""
In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.

You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.


"""

class Solution(object):
    def canIWin(self, maxChooseableInteger, desiredTotal):
        """
        :type maxChooseableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        dp = dict()
        def search(state, total):
            for x in range(maxChooseableInteger, 0, -1):
                if not state & (1<<(x-1)):
                    if total + x >= desiredTotal:
                        dp[state] = True
                        return True
                    break

            for x in range(1, maxChooseableInteger+1):
                if not state & (1<<(x-1)):
                    newstate = state | (1<<(x-1))
                    if newstate not in dp:
                        dp[newstate] = search(newstate, total+x)
                    if not dp[newstate]:
                        dp[state] = True
                        return True
            dp[state] = False
            return False

        if maxChooseableInteger >= desiredTotal: return True
        if (1+maxChooseableInteger) * maxChooseableInteger < 2 * desiredTotal:
            return False

        return search(0, 0)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-mc', type=int, help='maxChoosableInteger')
    parser.add_argument('-dt', type=int, help='desiredTotal')
    args = parser.parse_args()

    test = Solution()
    print test.canIWin(args.mc, args.dt)
