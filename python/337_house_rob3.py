#!/usr/bin/env python
# coding=utf-8
"""
 The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

 Determine the maximum amount of money the thief can rob tonight without alerting the police.

 Example 1:

         3
        / \
       2   3
        \   \ 
         3   1
    
    Maximum amount of money the thief can rob = 3 + 3 + 1 = 7. 

"""

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        valMap = {}

        def solve(root, path):
            if not root: return 0

            if path not in valMap:
                left, right = root.left, root.right
                ll = lr = rl = rr = None
                if left:
                    ll, lr = left.left, left.right
                if right:
                    rl, rr = right.left, right.right

                passup = solve(left, path +'l') + solve(right, path+'r')
                grabbit = root.val + solve(ll, path+'ll') + solve(lr, path+'lr') + solve(rl, path+'rl') + solve(rr, path + 'rr')
                valMap[path] = max(passup, grabbit)
            return valMap[path]

        return solve(root, '')

if __name__ == "__main__":

    test = Solution()
    nums = [3,2,3,None,3,None,1]
    test.rob()
