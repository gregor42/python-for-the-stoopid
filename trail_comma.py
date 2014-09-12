#!/usr/local/bin/python
#
#  trail_comma.py - an experiment in defining lists & the syntax thereof
#
import pri

# Say hello to the Nice People
pri.nt("Start.")
pri.nt(pri.line)


l1 = [1,2,3,4,5,6,7,8,]

pri.nt(l1)

l2 = [(1,2),(2,3),(4,5),]

pri.nt(l2)

pri.nt(l2[2][1])

pri.nt(l2[2])

#this will fail
#pri.nt(l2[3])

#this will fail
#pri.nt(l1[8])

pri.nt(pri.line)
pri.nt("Done.")


