#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2016/01/07/leetcode-sum-root-to-leaf-numbers/

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.

题目大意：
给定一棵只包含数字0-9的二叉树，每一条“根到叶子”路径表示一个数字。
一个“根到叶子”路径的例子是 1->2->3，表示数字123。
计算所有“根到叶子”数字的和。
测试用例如题目描述。

解题思路：
二叉树的深度优先搜索（DFS），详见代码。

"""

class Solution(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(root, val):
            val = val*10 + root.val
            if (root.left or root.right) is None:
                return val
            sums = 0
            if root.left:
                sums += dfs(root.left, val)
            if root.right:
                sums += dfs(root.right, val)
            return sums
        
        if root is None:
            return 0
        return dfs(root, 0)

