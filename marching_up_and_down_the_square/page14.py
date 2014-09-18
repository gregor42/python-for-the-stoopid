#!/usr/bin/python
# A system information Gathering script
import subprocess
import pri

filename = 'page14.py'
# Say hello to the Nice People
pri.ntc(filename + " : Start.")
pri.bar()

def uname_fun():

  uname = "uname"
  uname_arg = "-a"
  print "Gathering system information with %s command:\n" % uname
  subprocess.call([uname, uname_arg])

def disk_fun():

  diskspace = "df"
  diskspace_arg = "-kh"
  print "Gathering diskspace information %s command:\n" % diskspace
  subprocess.call([diskspace, diskspace_arg])

def main():
  uname_fun()
  disk_fun()

if __name__ == "__main__":
  main()
  pri.bar()
  pri.ntc("Done.")



