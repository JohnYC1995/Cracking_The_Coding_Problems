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

	def test_findRepeatedDnaSequences(self, solution):
		test = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
		self.sresult("findRepeatedDnaSequences - medium", solution.findRepeatedDnaSequences(test))
	
	def test_isAnagram(self, solution):
		s = "anagram"
		t = "nagaram"
		self.sresult("isAnagram - easy", solution.isAnagram(s,t))

	def test_getHint(self, solution):
		secret='180332'
		guess ='182341'
		self.sresult("getHint - medium", solution.getHint(secret, guess))

	def test_fourSumCount(self, solution):
		A = [ 1, 2]
		B = [-2,-1]
		C = [-1, 2]
		D = [ 0, 2]
		self.sresult("fourSumCount - medium", solution.fourSumCount(A,B,C,D))


