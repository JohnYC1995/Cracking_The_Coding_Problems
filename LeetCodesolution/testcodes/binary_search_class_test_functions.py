'''
!/usr/bin/python
 -*- coding: utf-8 -*-
 This is binary search class test function for Leetcode questions
 @ author Yongjun Chen
LeetCode
'''
class backtracking_search_class_Test_func(object):
	def __init__(self):
		self.index = 1

	def pname(self, name):
		result = '==================DFS '+str(self.index)+ '.' + str(name)  + '=================='
		print(result)

	def sresult(self, name, *args):
		self.pname(name)
		self.index += 1
		print(args)
		
	def test_readBinaryWatch(self, solution):
		test = 1
		self.sresult("readBinaryWatch - easy", solution.readBinaryWatch(test))