#!/usr/local/bin/python
#stringy.py
import pri 
    
filename = 'stringy.py'
# Say hello to the Nice People
pri.nt(filename + " : Start.")
pri.bar()

s1 = 'abcdefghijklmnopqrstuvwxyz'

s2 = s1[12:21]


print 1
print s1
print 2
print s2
print 3
# this will not work
print s1[-10:-20]
print 4
print s1[-20:-10]

pri.bar()
pri.ntc("Done.")

