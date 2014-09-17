#!/usr/local/bin/python
# 
#  instanceOne.py - an exercise in instantiating objects from classes
#
import pri

filename = 'instanceOne.py'

# Say hello to the Nice People
pri.ntc(filename + " : Start.")
pri.bar()

# Your code here
from ClassOne import * #get classes from ClassOne file
myBuddy = Calculator() # make myBuddy into a Calculator object
myBuddy.add(2) #use myBuddy's new add method derived from the Calculator class
print(myBuddy.getCurrent()) #print myBuddy's current instance variable 

myBuddy.add(40)
print(myBuddy.getCurrent())

pri.bar()
pri.ntc("Done.")


