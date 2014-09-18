#!/usr/local/bin/python
import pri

filename = 'numlen.py'
# Say hello to the Nice People
pri.ntc(filename + " : Start.")
pri.bar()


n = (42 ** 42 ** 2)/8675309


print n

print len(str(n))

print '-=-=-=-=-=-=-=-=-'

print len(str(8675309 ** 42))

pri.bar()
pri.ntc('Done.')
