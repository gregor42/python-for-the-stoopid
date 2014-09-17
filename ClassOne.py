#!/usr/local/bin/python

#ClassOne.py
class Calculator(object):

    #define class to simulate a simple calculator
    def __init__ (self):

        #start with zero
        self.current = 0

    def add(self, amount):

        #add number to current
        self.current += amount

    def getCurrent(self):

        return self.current
