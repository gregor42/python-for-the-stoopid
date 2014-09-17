#!/usr/local/bin/python

import sys
import pri

pri.ntc("Start: early-thrashing.py")
pri.bar() 

print(sys)
line = '-=-=-=-'
print(line)
d = dir(sys)
print d
print(line)
print(2 ** 100)
print(line)
x = 'Spam! '
print(x * 8)
print(line)

pri.bar()
pri.ntc("Done.")

