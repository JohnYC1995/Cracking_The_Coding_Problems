#!/usr/bin/python
# -*- coding: utf-8 -*-
# This is Listy class for 10.3
# author Yongjun Chen

class Listy(object):
	def __init__(self,listdata):
		self.list = listdata

	def elementAt(self,i):
		if i >= len(self.list):
			return -1
		else:
			return self.list[i]
	def show(self):
		print(self.list)
