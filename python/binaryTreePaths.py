#!/usr/bin/env python
# coding=utf-8

import argparse


"""
Given a binary tree, return all root-to-leaf paths.
https://leetcode.com/problems/binary-tree-paths/
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.ans = []
        if not root:
            return self.ans

        def dfs(root, path):
            if root.left is None and root.right is None:
                self.ans += path,
            if root.left:
                dfs(root.left, path+'->'+str(root.left.val))
            if root.right:
                dfs(root.right, path+'->'+str(root.right.val))
        dfs(root, str(root.val))
        return self.ans

    def binaryTreePaths2(self, root):
        if not root:
            return []
        return [str(root.val) + '->' + path for kid in (root.left, root.right) for path in self.binaryTreePaths2(kid)] or [str(root.val)]

    def binaryTreePaths3(self, root):
        res = []
        if not root:
            return res

        from collections import deque
        queue = deque([root, str(root.val)])
        while queue:
            front, path = queue.popleft()
            if front.left is None and front.right is None:
                res += path,
                continue
            if front.left:
                queue += [front.left, path+'->'+str(front.left.val)]
            if front.right:
                queue += [front.right, path+'->'+str(front.right.val)]
        return res
