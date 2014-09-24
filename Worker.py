#!/usr/local/bin/python
#
# Worker.py - an example using classes
#
import pri

filename = 'templ8.py'

# Say hello to the Nice People
pri.ntc(filename + " : Start.")
pri.bar()

class Worker:
  def __init__(self, name, pay):
    self.name = name
    self.pay = pay
  def surname(self):
    return self.name.split()[-1]
  def giveRaise(self, percent):
    self.pay *= (1.0 + percent)



pri.bar()
pri.ntc("Done.")


