'''
!/usr/bin/python
 -*- coding: utf-8 -*-
 This is two pointers test function for Leetcode questions
 @ author Yongjun Chen
LeetCode
'''
from two_pointers_class import *
class two_pointer_class_Test_func(object):
	def __init__(self):
		self.index = 1
	def pname(self, name):
		result = '==================DFS '+str(self.index)+ '.' + str(name)  + '=================='
		print(result)

	def sresult(self, name, *args):
		self.pname(name)
		self.index += 1
		print(args)

	def test_threesum(self, solution):
		test = [-1,0,1,-2,0,2]
		self.sresult("Threesum - Medium",solution.threeSum(test))

	def test_threeSumClosest(self, solution):
		test = [1,1,1,0]
		self.sresult("threeSumClosest - Medium", solution.threeSumClosest(test,100))
		self.sresult("threeSunClosest_my - mdedium", solution.threeSunClosest_my(test,100))

	def test_foursum(self, solution):
		test = [1,2,2,1,7,5]
		self.sresult("fourSum - Medium", solution.fourSum(test,6))

	def test_sortColors(self, solution):
		test = [0,1,2,1,0,2,1]
		self.sresult("sortColors - Medium", solution.sortColors(test))

	def test_removeDuplicates(self, solution):
		test = [1,1,1,3,3,3,4,4,5,5,6,6,7,7,8]
		self.sresult("removeDuplicates - Medium", solution.removeDuplicates(test))

	def test_removeDuplicates_part(self, solution):
		test = [1,1,1,3,3,3,4,4,5,5,6,6,7,7,8]
		self.sresult("removeDuplicates_part -Medium", solution.removeDuplicates_part(test))