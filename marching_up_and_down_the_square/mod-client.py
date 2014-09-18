#!/usr/local/bin/python

import fib
import pri

filename = 'mod-client.py'
# Say hello to the Nice People
pri.ntc(filename + " : Start.")
pri.bar()


fib.fib(1000000)

pri.bar()
pri.ntc("Done.")
