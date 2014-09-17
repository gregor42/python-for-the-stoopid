#!/usr/local/bin/python
#
#  console_width.py - quickly display what 80 columns looks like
#
#
import pri

filename = 'console_width.py'
# Say hello to the Nice People
pri.nt(filename + " : Start.")
pri.bar()

pri.nt(((' '*9)+('1'*10)+('2'*10)+('3'*10)+('4'*10)+('5'*10)+('6'*10)+('7'*10)+'8'))

pri.nt(('1234567890' * 8))

pri.bar()
print "Done."


