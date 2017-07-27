#!/usr/bin/env python
# coding=utf-8


"""
LeetCode 472. Concatenated Words

Given a list of words, please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:

    Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

http://bookshadow.com/weblog/2016/12/18/leetcode-concatenated-words/

"""

import argparse
from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = Counter(s)
        res = [k*v for (k, v) in cnt.most_common()]
        return ''.join(res)

    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        self.wordSet = set(words)
        for word in words:
            self.wordSet.remove(word)
            if self.search(word):
                ans.append(word)
            self.wordSet.add(word)
        return ans

    def search(self, word):
        if word in self.wordSet:
            return True
        for idx in range(1, len(word)):
            if word[:idx] in self.wordSet and self.search(word[idx:]):
                return True
        return False

if __name__ == "__main__":

    test = Solution()
    words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    res = test.findAllConcatenatedWordsInADict(words)
    print ' '.join(res)
#    parser = argparse.ArgumentParser()
#    parser.add_argument('s', type=str, help='input a string to be sort')
#    args = parser.parse_args()
#    print test.frequencySort(args.s)
