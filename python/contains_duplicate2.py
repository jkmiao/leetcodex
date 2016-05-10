#!/usr/bin/env python
# coding=utf-8

from collections import OrderedDict

class Solution:

    def containsNearByDuplicate(self,nums,k):
        """
        利用dict映射
        """
        numDict = dict()
        for i in range(len(nums)):
            idx = numDict.get(nums[i])
            if idx>=0 and idx-i<=k:
                return True
            numDict[nums[i]] = i
        return False



    def containsNearbyAlmostDuplicate(self,nums,k,t):
        if k<1 or t<0:
            return False
        numDict = OrderedDict()

        for i in range(len(nums)):
            key = nums[i]/max(1,t)
            for m in (key,key-1,key+1):
                if m in numDict and abs(nums[i]-numDict[m])<=t:
                    return True
            numDict[key] = nums[i]

            if i>=k :
                numDict.popitem(last=False)
        return False
        


    def maximalSquare(self,matrix):
        """
        动态规划，dp[i][j],以i,j为右下角的最大面积边长
        """
        if not matrix:
            return 0
        m,n = len(matrix),len(matrix[0])

        dp = [[0]*n for i in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                dp[i][j] = matrix[i][j]
                if i and j and matrix[i][j]:
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                    ans = max(ans,dp[i][j])
        return ans*ans






if __name__ == "__main__":
    test = Solution()
    matrix = [[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]]
    print test.maximalSquare(matrix)

    print test.containsNearByDuplicate(matrix[1],1)
    print test.containsNearbyAlmostDuplicate([12,3,53,3,2,4],2,3)

