#!/usr/local/bin/python
#
#  a_shrubbery - this is a properly screwy sandbox
#
# Say hello to the Nice People
import pri 
    
filename = 'a_shrubbery.py'
# Say hello to the Nice People
pri.nt(filename + " : Start.")
pri.bar()

import sys 
import re
import fib

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
pri.bar()
pri.nt("Done.")



