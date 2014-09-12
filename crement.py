#!/usr/local/bin/python
#
#  crement.py - testing c-like [in|de]crement
#               And the results show that these simply do not work
#               in Python
#
import pri

# Say hello to the Nice People
pri.ntc("Start.")
pri.bar()

n = 1
pri.ntc(n)
#nope
#n++
pri.ntc('nothing')
pri.ntc(n)
pri.ntc('increment')
++n
pri.ntc(n)
pri.ntc
pri.ntc('nothing')
#nope
#n--
pri.ntc(n)
pri.ntc('decrement')
--n
pri.ntc(n)

pri.bar()
pri.ntc("Done.")


