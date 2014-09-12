#!/usr/local/bin/python
#
#  pri.py - a cheap way around the python 2.7/3.x thing
#
#
# Say hello to the Nice People

def nt(somestr):
  print str(somestr).center(80)


line = ("-=" * 39)+"-"

def bar():
  nt(line)
