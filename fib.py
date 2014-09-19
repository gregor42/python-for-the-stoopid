#!/usr/local/bin/python

def fib(n):
    a,b = 0,1
    while b < n:
        print b
        a,b = b, a+b

def flist(n):
    a,b = 0,1
    fl = []
    while b < n:
        fl.append(b)
        a,b = b, a+b

    return fl


