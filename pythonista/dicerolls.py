import random

def d(rolls,sides):
	total = 0
	for i in range(0,rolls):
		total = total + random.randint(1,sides)	
	return total

average = 0	
count = 0
total = 0
for n in range(0,5):
	r = d(3,6)
	count=count+1
	total = total + r
	average = total/count
	print 'attribute:',r,' count:',count,' average:',average
print '---',average
  
  
