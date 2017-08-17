'''
!/usr/bin/python
 -*- coding: utf-8 -*-
 This is hash table class test function for Leetcode questions
 @ author Yongjun Chen
LeetCode
'''

class binary_search_class_Test_func(object):
	def __init__(self):
		self.index = 1

	def pname(self, name):
		result = '==================DFS '+str(self.index)+ '.' + str(name)  + '=================='
		print(result)

	def sresult(self, name, *args):
		self.pname(name)
		self.index += 1
		print(args)

	def test_guessNumber(self, solution):
		test = 10
		self.sresult("guessNumber - easy", solution.guessNumber(test))

	def test_searchMatrix(self,solution):
		test = [
  			[1,   3,  5,  7],
  			[10, 11, 16, 20],
  			[23, 30, 34, 50]
				]
		target = 3
		self.sresult("searchMatrix - medium", solution.searchMatrix(test,target))

	def test_findMin(self, solution):
		test = [4,5,6,7,9,1,2]
		self.sresult("findMin - medium", solution.findMin(test))

	def test_findPeakElement(self, solution):
		test = [1, 2, 3, 1]
		self.sresult("findPeakElement - medium", solution.findPeakElement(test))

	def test_findPeakElement2(self, solution):
		test = [1, 2, 3, 5,3,4,3,2,1]
		self.sresult("findPeakElement - medium", solution.findPeakElement2(test))

	def test_searchMatrix2(self, solution):
		test = [
  				[1,   4,  7, 11, 15],
  				[2,   5,  8, 12, 19],
  				[3,   6,  9, 16, 22],
  				[10, 13, 14, 17, 24],
  				[18, 21, 23, 26, 30]
				]
		target = 5
		self.sresult("searchMatrix2 - medium", solution.searchMatrix2(test,target))








