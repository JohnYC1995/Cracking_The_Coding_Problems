'''
!/usr/bin/python
 -*- coding: utf-8 -*-
 This is string test function for Leetcode questions
 @ author Yongjun Chen
LeetCode
'''
#Test function
class String_Test_func(object):
	def __init__(self):
		pass
	def pname(self, name):
		result = '==================' + str(name)  + '=================='
		print(result)
	def sresult(self, name, *args):
		self.pname(name)
		print(args)
	#------string-------#
	def test_romanToInt(self, solution):
		roman = 'MV'
		self.sresult("String 1.romanToInt - Easy", solution.romanToInt(roman))