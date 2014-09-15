#!/usr/local/bin/python
#
#  a_shrubbery - this is a properly screwy sandbox
#
# Say hello to the Nice People
print "Start."

import sys 
import re
import fib
import pri

line = (('-='*39)+'-').center(80)
n=4
rep = ('|....\'....'*n)+('+')+('....\'....|'*n)

pri.nt ('done importing...')

pri.nt(line)

pri.nt('sys.platform:'+sys.platform) 
pri.nt(line)

pri.nt('sys:'+str(sys))
pri.nt(line)
pri.nt('dir(sys):'+str(dir(sys)))
pri.nt(line)

pri.nt(2 ** 100)
x = 'Spam!'
pri.nt(line)

pri.nt(x * 8)
pri.nt(line)

for x in 'spam ':
   print(x) 

pri.nt(line)

fib.fib(1000)
print line


pri.nt(rep)
pri.nt(line)
pri.nt("Done.")



