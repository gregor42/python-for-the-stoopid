#!/usr/bin/env python
#A System Information Gathering Script
import subprocess
import pri

filename = 'ex1_2.py'
# Say hello to the Nice People
pri.ntc(filename + " : Start.")
pri.bar()

#Command 1
uname = "uname"
uname_arg = "-a"
print "Gathering system information with %s command:\n" % uname
subprocess.call([uname, uname_arg])

#Command 2
diskspace = "df"
diskspace_arg = "-h"
print "Gathering diskspace information %s command:\n" % diskspace
subprocess.call([diskspace, diskspace_arg])

pri.bar()
pri.ntc("Done.")
