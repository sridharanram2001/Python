class car:
	def milage(self,miles,litres):
		self.milage = miles*litres
	def print_stuff(self):
		print(self.milage)



mile = int(input("Enter the distance travelled by toyoto in miles "))
litres = int(input(("Enter the capcity of tank in litres "))
a=car()
a.milage(mile,litres)
a.print_stuff() 			