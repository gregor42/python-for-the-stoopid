import factor


def fun(x):
	return (x**2+2)
	
y = 0
	
for iteratio in list(range(10000000000,10000001111)):
	#z = fun(y)
  z = iteratio
  if len(factor.factors(z))==2:
    print(z,len(factor.factors(z)),factor.factors(z))
  y = z
