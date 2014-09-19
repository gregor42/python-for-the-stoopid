#!/usr/local/bin/python

import os
import random
import pri 
    
filename = 'pointed-stick.py'
# Say hello to the Nice People
pri.nt(filename + " : Start.")
pri.bar()

print('whoami? ')
print(os.getlogin())
print('whereami?')
print(os.getcwd())

s = 'This is a title that is being centered'
print(s.center(80))

print(s.upper().center(80))


s1 = 'This string will be reversed.'
print s1

print s1[::-1]


s2 = s1.replace('d.','yacious!')[::-1]

print s2


l1 = [1,2,3,4,5,6,7,10,42,420,42000,8999,9000,9001]
l2 = [random.random(),random.random(),random.random()]

print l1
print l2


pri.bar()
pri.ntc("Done.")

