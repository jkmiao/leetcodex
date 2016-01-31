#!/usr/bin/env python
# coding=utf-8


class Solution:
    
    def maxProduct(self,words):
        """
        :type words: List(str)
        :rtype: int
        """

        num = len(words)
        nums,len_map = [],[]
        for word in words:
            nums += sum( 1<<(ord(x)-ord("a")) for x in set(word)),
            len_map += len(word),
        
        ans = 0
        for i in range(num-1):
            for j in range(1,num):
                if not (nums[i] & nums[j]):
                    ans = max( len_map[i] * len_map[j], ans)
        return ans


if __name__ == "__main__":
    test = Solution()
    words = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"] 
    print test.maxProduct(words)
