#!/usr/bin/env python
# coding=utf-8

import sys
import random 

def longestIncSeq(nums):
    n = len(nums)
    dp = [1]*n
    for i in range(n):
        for j in range(i):
            if nums[i]>nums[j]:
                dp[i] = max(dp[i],dp[j]+1)

    return max(dp) if dp else 0


n = sys.argv[1]
nums = range(int(n))
random.shuffle(nums)
print nums
print longestIncSeq(nums)



    
