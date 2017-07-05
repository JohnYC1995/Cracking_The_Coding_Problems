'''
!/usr/bin/python
 -*- coding: utf-8 -*-
 This is array test function for Leetcode questions
 @ author Yongjun Chen
LeetCode
'''
#Test function
class Array_Test_func(object):
	def __init__(self):
		pass
	def pname(self, name):
		result = '==================' + str(name)  + '=================='
		print(result)
	def sresult(self, name, *args):
		self.pname(name)
		print(args)
	#---------Array---------#
	#1. twosum
	def test_twoSum(self, solution):
		nums = [2, 7, 11, 15]
		target = 9
		self.sresult("Array 1.twoSum - Easy",solution.twoSum(nums,target)) 
	#2. Remove Duplicates from Sorted Array
	def test_removeDuplicates(self, solution):
		nums = [1,1]
		self.sresult("Array 2.removeDuplicates - Easy",solution.removeDuplicates(nums))
	#3. removeElement
	def test_removeElement(self, solution):
		nums = [0,1,2,3,4,5,5]
		val = 3
		self.sresult("Array 3.removeElement - Easy", solution.removeElement(nums, val))
	#4. searchInsert
	def test_searchInsert(self, solution):
		nums = [1,2,2,3,4]
		val = 3
		self.sresult("Array 4.searchInsert - Easy", solution.searchInsert(nums,val))
	#5. maxSubArray
	def test_maxSubArray(self, solution):
		nums = [1,2,3,-2,-2,2]
		self.sresult("Array 5.maxSubArray - Easy", solution.maxSubArray(nums))
	#6. merge
	def test_merge(self, solution):
		list1 = [1,2,3,4]
		list2 = [7,8,9,2]
		self.sresult("Array 6.merge - Easy", solution.merge(list1,list2))
	#7. Pascal's Triangle
	def test_generate(self, solution):
		numRows = 6
		self.sresult("Array 7.generate - Easy", solution.generate(numRows))
	#8. test_getRow(self, solution):
	def test_getRow(self, solution):
		rowIndex = 4
		self.sresult("Array 8.getRow - Easy", solution.getRow(rowIndex))
	#9. Best Time to Buy and Sell Stock
	def test_maxProfit(self, solution):
		list1 = [7,2,5,11]
		self.sresult("Array 9.maxProfit - Easy", solution.maxProfit(list1))
	#10. Best Time to Buy and Sell Stock II
	def test_maxProfit2(self, solution):
		list1 = [2,5,5]
		self.sresult("Array 10.maxProfit2 - Easy", solution.maxProfit2(list1))
	#11. 
	def test_twoSum2(self, solution):
		list1 = [2,5,6]
		self.sresult("Array 11. twoSum2 - Easy", solution.twoSum2(list1,8))
	#12. Majority Element
	def test_majorityElement(self, solution):
		list1 = [1,2,2,2,3]
		self.sresult("Array 12. majorityElement - Easy", solution.majorityElement(list1))
	#13. Rotate Array
	def test_rotate(self, solution):
		Array = [1,2,3,4]
		self.sresult("Array 13. Rotate Array - Easy", solution.rotate(Array,2,'Frist'))
		Array = [1,2,3,4]
		self.sresult("Array 13. Rotate Array - Easy", solution.rotate(Array,2,'Second'))
	#14. Contains Duplicate
	def test_containsDuplicate(self,solution):
		Array = [1,2,4,4]
		self.sresult("Array 14. Contains Duplicate - Easy", solution.containsDuplicate([1,2,4,4]))
	#15. missingNumber
	def test_missingNumber(self, solution):
		lists = [0,1,2,3,4]
		self.sresult("Array 15. missingNumber - Easy", solution.missingNumber(lists))
	#16. moveZeroes
	def test_moveZeroes(self, solution):
		lists = [0,1,2,3,0,3,4]
		self.sresult("Array 16. moveZeroes - Easy", solution.moveZeroes(lists))
	#17. thirdMax
	def test_thirdMax(self, solution):
		list1 = [1,2,-2147483648]
		self.sresult("Array 17. thirdMax - Easy", solution.thirdMax(list1))
	#18. Consective one's
	def test_findMaxConsecutiveOnes(self, solution):
		list1 = [1,1,0,1,1,1]
		self.sresult("Array 18. findMaxConsecutiveOnes - Easy", solution.findMaxConsecutiveOnes(list1))
	#19. findPairs
	def test_findPairs(self, solution):
		list1 = [1,3,1,5,4]
		self.sresult("Array 19. findPairs - Easy", solution.findPairs(list1,0))
	#20. arrayPairSum
	def test_arrayPairSum(self, solution):
		list2 = [1,4,3,2]
		self.sresult("Array 20. arrayPairSum - Easy", solution.arrayPairSum(list2))
if __name__ == '__main__':
	pass
