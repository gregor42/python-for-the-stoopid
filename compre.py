#!/usr/local/bin/python
#
# compre.py - I need to learn about comprehensions
#
import pri

# Say hello to the Nice People
pri.ntc("Start.")
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

pri.bar()
pri.ntc("Done.")


