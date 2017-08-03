'''
!/usr/bin/python
 -*- coding: utf-8 -*-
 This is math class test function for Leetcode questions
 @ author Yongjun Chen
LeetCode
'''
from two_pointers_class import *
class math_class_Test_func(object):
	def __init__(self):
		self.index = 1
	def pname(self, name):
		result = '==================DFS '+str(self.index)+ '.' + str(name)  + '=================='
		print(result)

	def sresult(self, name, *args):
		self.pname(name)
		self.index += 1
		print(args)

	def test_mySqrt(self, solution):
		test = 4
		self.sresult("mySqrt - easy", solution.mySqrt(test,2))

	def test_isPowerOfTwo(self, solution):
		test = 8
		self.sresult("isPowerOfTwo - easy", solution.isPowerOfTwo(test))

	def test_isUgly(self, solution):
		test = 8
		self.sresult("isUgly - easy", solution.isUgly(test))

	def test_isPerfectSquare(self, solution):
		test = 25
		self.sresult("isPerfectSquare - easy", solution.isPerfectSquare(test))

	def test_maxRotateFunction(self, solution):
		test = [4, 3, 2, 6]
		self.sresult("maxRotateFunction - medium", solution.maxRotateFunction(test))

	def test_integerReplacement(self, solution):
		test = 7
		self.sresult("integerReplacement - medium", solution.integerReplacement(test))

	def test_minMoves2(self, solution):
		test = [1,2,3,5,6]
		self.sresult("minMoves2 - medium", solution.minMoves2(test))