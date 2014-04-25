class Integer(object):
	def __init__(self, number_to_set,NorP ):
		self.number = number_to_set
		self.NorP = NorP
	
	def display(self):
		if self.NorP == False:
			print "-" + str(self.number)
		else:
			print "+" + str(self.number)

class NegativeInteger(Integer):
 	def __init__(self, number_to_set):
 		 super(NegativeInteger, self).__init__(number_to_set, False)

 	def display(self):
 		print "-" + str(self.number)
 		print " This is a Negative Integer."

if __name__ =="__main__":
	x = Integer(55555, False)
	z = NegativeInteger(800)
	x.display()
	z.display()




# class Integer(object):
# 	def __init__(self, number_to_set=""):
# 		self.number = number_to_set

# 	def display(self):
# 		print self.number

# if __name__=="__main__":
# 	x = Integer(300)
# 	x.display()
