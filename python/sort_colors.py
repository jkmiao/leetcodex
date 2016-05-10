#!/usr/bin/env python
# coding=utf-8


class Solution:

    def sortColors(self,nums):

        n = len(nums)
        if n<2:
            return nums

        for i in range(1,n):
            value = nums[i]
            j = i-1
            while j>=0 and nums[j]>value:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = value
        return nums



    def sortColors2(self,nums):

        res = {"0":[],"1":[],"2":[]}
        for v in nums:
            if v==0:
                res["0"].append(v)
            elif v==1:
                res["1"].append(v)
            else:
                res["2"].append(v)
        nums[:] = res["0"]+res["1"]+res["2"]



if __name__=="__main__":
    import numpy as np
    test = Solution()
    input = np.random.randint(0,3,10)
    print input
    output = test.sortColors2(input)
    print output
    print input

