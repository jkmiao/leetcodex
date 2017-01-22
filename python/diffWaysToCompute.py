#!/usr/bin/env python
# coding=utf-8

import re
import argparse


"""
字符串任意加括号改变计算顺序，获取所有可能计算结果
"""


class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        return [a+b if c=='+' else a-b if c=='-' else a*b
                for i, c in enumerate(input) if c in '+-*'
                for a in self.diffWaysToCompute(input[:i])
                for b in self.diffWaysToCompute(input[i+1:])] or [int(input)]

    def diffWaysToCompute2(self, input):
        def calc(a, b, o):
            return {'+': lambda x,y: x+y,
                    '-': lambda x,y: x-y,
                    '*': lambda x,y: x*y}[o](a,b)

        def dfs(nums, ops):
            if not ops:
                return [nums[0]]

            ans = []
            for x in range(len(ops)):
                left = dfs(nums[:x+1], ops[:x])
                right = dfs(nums[x+1:], ops[x+1:])
                for l in left:
                    for r in right:
                        ans.append(calc(l, r, ops[x]))

            return ans

        nums, ops = [], []
        input = re.split(r'(\D)', input)
        for x in input:
            if x.isdigit():
                nums.append(int(x))
            else:
                ops.append(x)

        return dfs(nums, ops)

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--input',help="string of numbers and operators")
    args = parser.parse_args()
    test = Solution()
    print test.diffWaysToCompute(args.input)
    print test.diffWaysToCompute2(args.input)
