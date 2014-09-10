#!/usr/local/bin/python

line =  "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
print line
print 'import begins...'

import fib
import randy

# this doesn't work because of the '-' character:
#import pointed-stick

print "import complete."
print line


them = "ex1_3.sh		myfile.py		page14.py		pwd.py			stringy.py		whatsyssy.py brian			fib.py			myfile.pyc		page3.pl		pyfun.py		textadd.py		zen.py built-in-objs.py	hello_world.py		newline.py		page3.py		pyfun_lesson.txt	threenames.py	early-thrashing.py	maths.py		numlen.py		page3.sh		randy.py		threenames.pyc ex1_2.py		mod-client.py		os.py			pointed-stick.py	reverse_fail.py		touch-timer.py"
print them
print line
those = them.replace(' ',"").replace("\t",",").replace(",,",",").replace(",,",",")
print those
print line
print them.replace("\w",",")
print line
d1 = dir(fib)
print d1
print line

d2 = dir(randy)
print d2
print line

d3 = dir(them)
print d3
print line

fib.fib(1000000)
print line
li = those.split(',')
print li
print line

print 'Done.'

