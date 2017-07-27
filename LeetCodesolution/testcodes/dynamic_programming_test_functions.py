'''
!/usr/bin/python
 -*- coding: utf-8 -*-
 This is dynamic programming test function for Leetcode questions
 @ author Yongjun Chen
LeetCode
'''
from DP_NumArray_class import * 
#Test function
class Dynamic_Programming_Test_func(object):
	def __init__(self):
		self.index = 1
	def pname(self, name):
		result = '==================DP '+str(self.index)+ '.' + str(name)  + '=================='
		print(result)
	def sresult(self, name, *args):
		self.pname(name)
		self.index += 1
		print(args)
	def test_maxSubArray(self, solution):
		nums = [1,2,3,-2,-2,2]
		self.sresult( "maxSubArray - Easy", solution.maxSubArray(nums))
	def test_rob(self, solution):
		nums = [3,4,5,6,7,8,9]
		self.sresult("rob - Easy", solution.rob(nums))
	def test_range_sum_query(self):
		nums = [1,2,3,4,5]
		test = NumArray(nums)
		self.sresult("range_sum_query - Easy",test.sumRange(0,2),\
			test.sumRange(1,2),test.sumRange(2,4))
	#-------Median-------#
	def test_uniquePaths(self, solution):
		self.sresult("uniquePaths - Median", solution.uniquePaths(3,3))
	def test_minPathSum(self, solution):
		grid =[[1,2,3],[2,3,1]]
		self.sresult("minPathSum - Median", solution.minPathSum(grid))
	def test_numTrees(self, solution):
		self.sresult("numTrees - Median", solution.numTrees(6))

