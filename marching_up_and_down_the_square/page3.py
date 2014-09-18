#!/usr/bin/env python

import os

if os.path.isdir("/tmp"):
#if os.isdir("/tmp"):
  print "/tmp is a directory"
else:
  print "/tmp is not a directory"

