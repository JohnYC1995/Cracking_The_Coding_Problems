'''
!/usr/bin/python
 -*- coding: utf-8 -*-
 This is main function for Leetcode questions
 @ author Yongjun Chen
LeetCode
'''
from array_class import * 
from array_test_functions import *
from string_class import *
from string_test_functions import *
from dynamic_programming_class import *
from dynamic_programming_test_functions import *
from Depth_first_Search_class import *
from Depth_first_Search_class_test_functions import *
import pdb
def array_test(solution, test_solution):
	test_solution.test_twoSum(solution)
	test_solution.test_removeDuplicates(solution)
	test_solution.test_removeElement(solution)
	test_solution.test_searchInsert(solution)
	test_solution.test_maxSubArray(solution)
	test_solution.test_generate(solution)
	test_solution.test_getRow(solution)
	test_solution.test_maxProfit(solution)
	test_solution.test_maxProfit2(solution)
	test_solution.test_twoSum2(solution)
	test_solution.test_majorityElement(solution)
	test_solution.test_rotate(solution)
	test_solution.test_containsDuplicate(solution)
	test_solution.test_missingNumber(solution)
	test_solution.test_moveZeroes(solution)
	test_solution.test_thirdMax(solution)
	test_solution.test_findMaxConsecutiveOnes(solution)
	test_solution.test_findPairs(solution)
	test_solution.test_arrayPairSum(solution)

def string_test(solution, test_solution):
	test_solution.test_romanToInt(solution)
	test_solution.test_isValid(solution)
	test_solution.test_lengthOfLastWord(solution)
	test_solution.test_reverseString(solution)
	test_solution.test_countSegments(solution)
	test_solution.test_lengthOfLongestSubstring(solution)

def dynamic_programming_test(solution, test_solution):
	test_solution.test_maxSubArray(solution)
	test_solution.test_rob(solution)
	test_solution.test_range_sum_query()
	test_solution.test_uniquePaths(solution)
	test_solution.test_minPathSum(solution)
	test_solution.test_numTrees(solution)#good one

def depth_first_search_test(solution, test_solution):
	test_solution.test_isSameTree(solution)
	test_solution.test_isSymmetric(solution)
	test_solution.test_maxDepth(solution)
	test_solution.test_sortedArrayToBST(solution)
	
def main():
	#array_test(Array(),Array_Test_func())
	#string_test(String(),String_Test_func())
	#dynamic_programming_test(dynamic_programming(),Dynamic_Programming_Test_func())
	depth_first_search_test(Depth_first_Search(),Depth_first_Search_Test_func())
if __name__ == '__main__':
	main()

