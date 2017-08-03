'''
!/usr/bin/python
 -*- coding: utf-8 -*-
 This is hash table class test function for Leetcode questions
 @ author Yongjun Chen
LeetCode
'''

class hash_table_class_Test_func(object):
	def __init__(self):
		self.index = 1

	def pname(self, name):
		result = '==================DFS '+str(self.index)+ '.' + str(name)  + '=================='
		print(result)

	def sresult(self, name, *args):
		self.pname(name)
		self.index += 1
		print(args)

	def test_singleNumber(self, solution):
		test = [1,1,2,2,3,3,4,5,5,6,6]
		self.sresult("singleNumber - easy", solution.singleNumber(test))