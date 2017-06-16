

from VehicleSize import *


class Vehicle(object):

	def __init__(self):
		self.size = VehicleSize()
		self.spotsNeeded = int
		self.parkingSpots = []

	def get_size(self):
		return self.size

	def getSpotsNeeded(self):
		return self.spotsNeeded

	def parkinSpot(self,s):
		self.parkingSpots.append(s)

	def clearSpots(self):

	def canFitinSpot(self,s):
		

if __name__ == '__main__':
	V = Vehicle()
	print(V.spotsNeeded)