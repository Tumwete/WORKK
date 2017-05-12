class Work():
	def __init__(self):
		self.str=str
	def getString(self):
		self.str=input('please enter your string here: ')
		print(self.str)
	def printString(self):
		print (self.str.upper())
def testi():
	return type(w.getString)
	return type(w.printString)
	

w=Work()
w.getString()
w.printString()
k=testi()
# print(k)



