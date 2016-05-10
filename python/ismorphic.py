#!/usr/bin/env python
# coding=utf-8

import sys

def isomorphic(s,t):
    if len(s)!=len(t):
        return False

    s2t,t2s = {},{}

    for i in range(len(s)):
        source,target = t2s.get(t[i]),s2t.get(s[i])
        if source is None and target is None:
            t2s[t[i]],s2t[s[i]] = s[i],t[i]
        elif target != t[i] or source != s[i]:
            return False
    return True

s = sys.argv[1]
t = sys.argv[2]

print isomorphic(s,t)
