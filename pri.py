#!/usr/local/bin/python
#
#  pri.py - a cheap way around the python 2.7/3.x thing
#
#

def nt(somestr):
  print str(somestr)

def ntc(somestr):
  print str(somestr).center(80)


line = ("-=" * 39)+"-"

def bar():
  ntc(line)
