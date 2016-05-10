#!/usr/bin/env python
# coding=utf-8


import random

class Solution:
    # @param { integer[] } nums
    # @param { integer } k
    # @return { integer }

    def findKthLargest(self,nums,k):
        """
        O(n)
        """

        pivot = random.choice(nums)
        nums1,nums2 = [],[]

        for num in nums: 
            if num>pivot:
                nums1.append(num)
            elif num<pivot:
                nums2.append(num)

        if k <= len(nums1):
            return self.findKthLargest(nums1,k)
        if k > len(nums)-len(nums2):
            return self.findKthLargest(nums2,k-(len(nums)-len(nums2)))
        return pivot


    def findKthLargest2(self,nums,k):
        """
        O(nlog(n))
        """
        return sorted(nums,reverse=True)[k-1]
