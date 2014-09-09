#!/usr/local/bin/python

import os

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

print 'Done.'


