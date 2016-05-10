#!/usr/bin/env python
# coding=utf-8


class Solution(object):

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        for i, c in enumerate(sorted(citations, reverse=True)):
            if i>= c:
                return i

        return len(citations)



    def hIndex2(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        return sum(i<c for i,c in enumerate(sorted(citations, reverse = True)))
