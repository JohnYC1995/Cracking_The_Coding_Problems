#!/usr/bin/python
# -*- coding: utf-8 -*-
# This is a queue class
# author Yongjun Chen

from Mystack import *

class Myqueue(object):

	def __init__(self):
		self.stack1 = Mystack()
		self.stack2 = Mystack()

	def push(self,item):
		self.stack1.push(item)

	def pop(self):
		for index in range(self.stack1.size()):
			self.stack2.push(self.stack1.pop())
		result = self.stack2.pop()
		self.stack1.push(self.stack2.pop())
		return result

	def peek(self):
		for index in range(self.stack1.size()):
			self.stack2.push(self.stack1.pop())
		result = self.stack2[0]
		self.stack1.push(self.stack2.pop())
		return result




