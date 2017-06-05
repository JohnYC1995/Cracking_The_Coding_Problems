#!/usr/bin/python
# -*- coding: utf-8 -*-
# This is a stack class
# author Yongjun Chen

class Mystack(object):

	def __init__(self):
		self.items = []
		self.min = []

	def push(self, item):
		self.items.append(item)
		if len(self.min) == 0 or self.min[-1] > item:
			self.min.append(item)

	def pop(self):
		if self.items[-1] == self.min[-1]:
			self.min.pop()
		if len(self.items) < 0:
			print("the stack is empty")
			return
		return self.items.pop()

	def get_min(self):
		if len(self.min) == 0:
			print("stack is empty ")
		return self.min[-1]

	def clear(self):
		del self.items[:]

	def size(self):
		return len(self.items)

	def isEmpty(self):
		if len(self.items) == 0:
			return True 
		else:
			return False
	def show_stack(self):
		for index in range(len(self.items)):
			print(self.items[index])
	def peek(self):
		return self.items[len(self.items)-1]

