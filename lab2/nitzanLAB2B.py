def ispalindrome():
	x=raw_input("type something:")
	y=len(x)
	answer=""
	for z in range (y-1, 0-1, -1):
		answer+=x[z]
	
	if x==answer:
		print "true"
	else:
		print "false"
