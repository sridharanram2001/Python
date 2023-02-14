class car:
	def __init__(self,model,milage,seats):
		self.model_name=model
		self.car_milage=milage
		self.car_seats=seats
	def show_data(self):
		print(f"The model name of this car is {self.model_name}")
		print("\n")
		print(f"The milage of this car is {self.car_milage}")
		print("\n")
		print(f"The car has {self.car_seats} seats")


Toyoto=car("Innova","100 litres/km",6)
Skoda=car("Fabia","120 litres/km",4)
Toyoto.show_data()
Skoda.show_data()