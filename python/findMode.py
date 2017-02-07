#!/usr/bin/env python
# coding=utf-8

from collections import Counter

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        counter = Counter()

        def traverse(root):
            if not root:
                return
            counter[root.val] += 1
            traverse(root.left)
            traverse(root.right)

        traverse(root)
        maxn = max(counter.values() + [None])
        return [k for k, v in counter.iteritems() if v == maxn]
