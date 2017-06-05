#!/usr/bin/python
# -*- coding: utf-8 -*-
# This is a circlelist class, not finish
# author Yongjun Chen
from Node import *

class CircleList(object):
	def __init__(self):
		self.headNode = Node(None)
		self.headNode.next = self.headNode
		self.head = self.headNode
		self.size = 0
	# be called when print the class
	def __str__(self):
		if self.size == 0:
			return 'Empty'
		s = ''
		fin = self.head.next.next
		while fin.value:
			s += str(fin.value)  
			if fin.next.value:  
				s += ','  
			fin = fin.next
		return s
	def addelement(self,value):
		elementNode = Node(value)
		#It's a empty list
		if self.head.value = None:
			pass
			