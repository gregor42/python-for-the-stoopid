#!/usr/loca/bin/python

import os
import pri

filename = 'os.py'
# Say hello to the Nice People
pri.ntc(filename + " : Start.")
pri.bar()

d = dir(os)

print(d)

pri.bar()
pri.ntc("Done.")
