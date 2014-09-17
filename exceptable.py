#!/usr/local/bin/python
#
#  exceptable.py - an exercise in exception handling
#
import pri

filename = 'exceptable.py'

# Say hello to the Nice People
pri.ntc(filename + " : Start.")
pri.bar()


n = '42' # the quotes make this a string
try:
    n = n + 1 #string vs. number addition error here 
except:
    pri.ntc(n + " is not a number") #the expected result

print(n) 

pri.bar()
pri.ntc("Done.")


