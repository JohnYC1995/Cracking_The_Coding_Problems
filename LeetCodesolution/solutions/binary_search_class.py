'''
!/usr/bin/python
 -*- coding: utf-8 -*-
 This is binary search class solution for Leetcode questions
 @ author Yongjun Chen
LeetCode
'''
#leetcode solutions
import random 
class binary_search(object):
	def __init__(self):
		self.N = random.randint(0,100000)

	def searchMatrix(self, matrix, target):
		if not matrix or not matrix[0]:
			return False
		row,column = len(matrix), len(matrix[0])
		low, high = 0, row*column - 1
		while low <= high:
			mid = (low + high) // 2
			num = matrix[mid//column][mid%column] 
			if num == target:
				return True
			elif num < target:
				low = mid + 1
			else:
				high = mid - 1
		return False

	def findMin(self, nums):
		low, high = 0, len(nums)-1
		while low < high:
			mid = (low + high) // 2
			if nums[mid] > nums[high]:
				low = mid + 1
			else:
				high = mid
		return nums[low]

	def search(self, nums, left, right):
		if left == right:
			return left
		mid = (left + right) // 2
		if nums[mid] > nums[mid+1]:
			return self.search(nums,left, mid)
		else:
			return self.search(nums, mid+1, right)

	def findPeakElement(self, nums):
		return self.search(nums,0,len(nums)-1)

	def findPeakElement2(self, nums):
		left = 0
		right = len(nums)-1
		while left < right:
			mid = (left + right) // 2
			if nums[mid]>nums[mid+1]:
				right = mid
			else:
				left = mid + 1
		return left
	
	def searchMatrix2(self, matrix, target):
		if not matrix or not matrix[0]:
			return False	
		row = len(matrix)-1
		column = len(matrix[0])-1
		i, j = 0, column
		while i <= row and j >= 0:
			if matrix[i][j] == target:
				return True
			elif matrix[i][j] < target and i < row:
				i += 1
			else:
				j -= 1
		return False

	def guess(self,nums):
		if nums < 6:
			return 1
		elif nums == 6:
			return 0
		else:
			return -1

	def guessNumber(self, n):
		left = 0
		right = n
		while left <= right:
			mid = (right + left) // 2
			res = self.guess(mid)
			if res == 0:
				return mid
			elif res == 1:
				left = mid + 1
			else:
				right = mid -1
		return -1

if __name__ == '__main__':
	s = binary_search()
	matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
	target = 20
	print(s.guessNumber(10))
