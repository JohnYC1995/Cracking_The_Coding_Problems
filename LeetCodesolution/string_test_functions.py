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
		self.index = 1
	def pname(self, name):
		result = '==================String '+str(self.index)+ '.' + str(name)  + '=================='
		print(result)
	def sresult(self, name, *args):
		self.pname(name)
		self.index += 1
		print(args)
	#------string-------#
	def test_romanToInt(self, solution):
		roman = 'MV'
		self.sresult("romanToInt - Easy", solution.romanToInt(roman))
	def test_isValid(self, solution):
		test = "([)]"
		self.sresult("isValid - Easy", solution.isValid(test))
	def test_lengthOfLastWord(self, solution):
		test = 'a b ctest'
		self.sresult("lengthOfLastWord - Easy", solution.lengthOfLastWord(test))
	def test_reverseString(self, solution):
		test = 'Hello'
		self.sresult("reverseString - Easy", solution.reverseString(test))
	def test_countSegments(self, solution):
		test = "Hello, my name is John"
		self.sresult("countSegments - Easy", solution.countSegments(test))
	def test_lengthOfLongestSubstring(self, solution):
		test = 'c'
		self.sresult("lengthOfLongesetSubstring - Median", solution.lengthOfLongestSubstring(test))
