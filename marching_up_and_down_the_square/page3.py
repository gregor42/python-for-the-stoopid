#!/usr/bin/env python

import os
import pri 
    
filename = 'console_width.py'
# Say hello to the Nice People
pri.nt(filename + " : Start.")
pri.bar()

if os.path.isdir("/tmp"):
#if os.isdir("/tmp"):
  print "/tmp is a directory"
else:
  print "/tmp is not a directory"

pri.bar()
pri.ntc("Done.")


