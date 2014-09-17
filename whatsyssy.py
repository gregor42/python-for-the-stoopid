#!/usr/local/bin/python

import sys
import pri

filename = 'whatsyssy.pl'
pri.ntc(filename + " : Start.")
pri.bar()

print('Platform:  '+ sys.platform) 
print
print('Path:  ')
print(sys.path)
print
pri.bar()
print('done.')

