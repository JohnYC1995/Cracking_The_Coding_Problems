'''
!/usr/bin/python
 -*- coding: utf-8 -*-
 This is hash table class solution for Leetcode questions
 @ author Yongjun Chen
LeetCode
'''

#leetcode solutions
class hash_table(object):
	def __init__(self):
		pass

	def singleNumber(self, nums):
		result = nums[0]
		for i in range(1,len(nums)):
			result = result^nums[i]
		return result

if __name__ == '__main__':
	s = hash_table()
	print(s.singleNumber([1,1,2,2,3,3,4,5]))