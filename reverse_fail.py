#!/usr/local/bin/python
#
# So this was disappointing.  I thought perhaps that if you could
# multiply a string to make it repeat then maybe if you multiplied
# by a negative number then the string might be reversed.
# ::shrug::
# gregor42@mail.com

seq1 = '0123456789'
seq2 = '|=--.----'
seq3 = seq1 * 3
seq4 = seq1 * -1
seq5 = (seq2 * 2),'+',(seq2 * -2)

print(seq1)
print
print(seq2)
print
print(seq3)
print
print(seq4)
print
print(seq5)
print
print('done.')

