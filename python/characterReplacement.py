#!/usr/bin/env python
# coding=utf-8

import collections

class Solution(object):
    """
        给定一个只包含大写英文字母打字符串，可以将其中的任意字母用其他字母替换至多k次。计算替换完成之后可以得到打最大重复字母的长度.
        https://leetcode.com/problems/longest-repeating-character-replacement/
    """
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
      #  s = s.lower() 
        table = collections.Counter()
        res = 0
        p1, p2 = 0, 0
        while p2 < len(s):
            table[s[p2]] += 1
            p2 += 1
            while p2 - p1 - max(table.values()) > k:
                table[s[p1]] -= 1
                p1 += 1
            res = max(res, p2-p1)
        return res


if __name__ == "__main__":

    import sys
    s = sys.argv[1]
    k = int(sys.argv[2])
    test = Solution()
    print test.characterReplacement(s, k)

