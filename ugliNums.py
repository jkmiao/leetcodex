#!/usr/bin/env python
# coding=utf-8

def nthSuperUglyNumber(n,primes):
    size = len(primes)
    res = [0]*n
    idx = [0]*size
    vals = [0]*size
    res[0] = 1
    for i in range(1,n):
        for j in range(size):
            vals[j] = res[idx[j]]*primes[j]
        res[i] = min(vals)

        for j in range(size):
            if vals[j]==res[i]:
                idx[j]+=1

    return res[n-1]



for i in xrange(1,12):
    res = nthSuperUglyNumber(i,[2,7,13,19])
    print res

