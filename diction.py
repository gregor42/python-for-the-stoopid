#!/usr/local/bin/python
#
# diction.py - playing with dictionaries
#
import pri

filename = 'templ8.py'

# Say hello to the Nice People
pri.ntc(filename + " : Start.")
pri.bar()

D = {'a': 1, 'b': 2, 'c': 3}
pri.ntc(D)
pri.bar()

D['e']=42
pri.ntc(D)
pri.bar()

#underfined value will break
#print D['f']


pri.ntc('f' in D)
pri.bar()
if not 'f' in D: 
    pri.ntc("f is missing")
    pri.ntc("no really")

pri.bar()
pri.ntc(D.get('x',-1))

pri.bar()

Ks = list(D.keys())
pri.ntc(Ks)
pri.bar()

Ks.sort()
pri.ntc(Ks)
pri.bar()

for key in sorted(D):
    print(key, '=>', D[key])

pri.bar()
for c in 'spam spam spam':
    print(c.upper())

pri.bar()
x = 4
while x > 0:
    print('spam! ' * x)
    x -= 1

pri.bar()
pri.ntc("Done.")


