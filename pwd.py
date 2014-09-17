#!/usr/local/bin/python

import os
import pri

filename = 'pwd.py'
pri.ntc(filename + " : Start.")
pri.bar()

print(os.getcwd())

pri.bar()
pri.ntc("done.")
