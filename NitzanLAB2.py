def divisors(y):
	y=int(y)	
	for x in range(1,y+1):
		if y%x==0:
			print x
