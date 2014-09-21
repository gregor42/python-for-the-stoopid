#!/usr/local/bin/python
#
# compre.py - I need to learn about comprehensions
#
import pri
import fib

filename = 'compre.py'
# Say hello to the Nice People
pri.ntc(filename + " : Start.")
pri.bar()

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

pri.ntc(M)
pri.bar()

pri.ntc(M[1])
pri.bar()

pri.ntc(M[1][2])
pri.bar()

col = [row[1] for row in M]
pri.ntc(col)
pri.bar()

squares = [x ** 2 for x in range(5)]
pri.ntc(squares)
pri.bar()

sqli = [y ** 64 for y in fib.flist(42)]
pri.ntc(sqli)

pri.bar()

sq = []
for x in [1,2,3,4,5]:
    sq.append(x ** 2)

pri.ntc(sq)


pri.bar()
pri.ntc("Done.")


