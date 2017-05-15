#!/usr/bin/env python
# coding=utf-8

import sys

class Solution(object):

    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s.coutn('A')<=1 and 'LLL' not in s

    
