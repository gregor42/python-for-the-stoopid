#!/usr/local/bin/python
#
# loopy.py - I want to try out some loopage
#
import pri

filename = 'loopy.pl'

# Say hello to the Nice People
pri.ntc(filename + " : Start.")
pri.bar()

# Your code here

for x in range(43):
  pri.ntc(str(x) + " : " + str(bin(x)))


pri.bar()
pri.ntc("Done.")


