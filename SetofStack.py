#!/usr/bin/python
# -*- coding: utf-8 -*-
# This is a example of usage of singlelist class
# author Yongjun Chen

from Mystack import *


class SetofStack(object):

	def __init__(self,threshold):
		self.setofstack = {}
		self.items = []
		self.threshold = threshold
		self.stack_index = 0

	def push(self,item):
		if len(self.items) < self.threshold:
			self.items.append(item)
			self.setofstack[self.stack_index] = self.items
		else:
			self.stack_index += 1
			self.items = []
			self.items.append(item)
			self.setofstack[self.stack_index] = self.items

	def pop(self,index = None):
		if self.stack_index-1 == 0:
			print("the setofstack is empty")
		if len(self.items) > 0:
			return self.setofstack[self.stack_index].pop()
		else:
			self.stack_index-=1
			self.items = self.setofstack[self.stack_index]
			return self.setofstack[self.stack_index].pop()

	def show_stack(self):
		for index in range(len(self.items)):
			print(self.items[index])

	def show_setofstack(self):
		for stack_index in range(self.stack_index+1):
			print("====stack====:",stack_index)
			for index in range(len(self.setofstack[stack_index])):
				print(self.setofstack[stack_index][index])





