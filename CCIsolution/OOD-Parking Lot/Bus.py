from Vehicle import *


class Bus(Vehicle):

	def __init__(self):
		self.size = VehicleSize().Large
		self.spotsNeeded = 10



if __name__ == '__main__':
	b = Bus()
	print(b.get_size())