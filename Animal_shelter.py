#!/usr/bin/python
# -*- coding: utf-8 -*-
# This is a example of Singlelist usage class
# author Yongjun Chen
from SingleList import *

class Animal_Shelter(object):

	def __init__(self):
		self.item = LinkList()

	def enqueue(self,animal):
		self.item.append(animal)

	def isEmpty(self):
		if self.item.getlength() > 0:
			return False
		else:
			return True

	def dequeueAny(self):
		if self.item.getlength() == 0:
			print('There is no animal in shelter')
			return 
		else:
			return self.item.getitem(0)

	def dequeueDog(self):
		for index in range(self.item.getlength()):
			if self.item.getitem(index)[1] == 'dog':
				result = self.item.getitem(index)[0]
				break
		self.item.delete(index)
		return result

	def dequeueCat(self):
		for index in range(self.item.getlength()):
			if self.item.getitem(index)[1] == 'cat':
				result = self.item.getitem(index)[0]
				break
		self.item.delete(index)
		return result

	def show_animals(self):
		print(self.item.Return_Kth_to_Last(1))


