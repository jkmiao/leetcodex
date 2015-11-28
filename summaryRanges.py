#!/usr/bin/env python
# coding=utf-8

def summaryRanges(nums):
    if not nums:
        return []
    res = []
    
    i,size = 0,len(nums)
    
    while i<size:
        l,r = i,str(nums[i])
        while i+1<size and nums[i+1]-nums[i]==1:
            i += 1
        if i>l:
            r += '->' + str(nums[i])
        res.append(r)
        i += 1
    return res


class treeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def isSymmetric(root):
    if not root:
        return True
    return isSymmetric(root.left,root.right)


def isSymmetric2(left,right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    return left.val==right.val and isSymmetric2(left.left,right.right) and isSymmetric2(left.right,right.left)



