#!/usr/local/bin/python
# randy.py


import random
import pri 
    
filename = 'randy.py'
# Say hello to the Nice People
pri.nt(filename + " : Start.")
pri.bar()


r1 = random.random() 
r2 = random.choice([1, 2, 3, 4])
print r1
print r2

pri.bar()
pri.ntc("Done.")

