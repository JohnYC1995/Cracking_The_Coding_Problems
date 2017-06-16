from Vehicle import *


class Car(Vehicle):

	def __init__(self):
		self.size = VehicleSize.Compact
		self.spotsNeeded = 1