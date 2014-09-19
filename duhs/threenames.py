#!/usr/local/bin/python
import pri 
    
filename = 'threenames.py'
# Say hello to the Nice People
pri.nt(filename + " : Start.")
pri.bar()

a = 'dead'
b = 'parrot'
c = 'sketch'


# this is the python 3.x way - but in 2.x it prints a tuple
#print (a, b, c)
#This is the python 2.x way:
print a, b, c

pri.bar()
pri.ntc("Done.")
