'''
!/usr/bin/python
 -*- coding: utf-8 -*-
 This is main function for Leetcode questions
 @ author Yongjun Chen
LeetCode
'''
import sys
sys.path.append("/Users/Juhn/Desktop/Coding_Learn/leetcode/solutions")
from solutions.array_class import * 
from solutions.string_class import *
from solutions.dynamic_programming_class import *
from solutions.Depth_first_Search_class import *
from solutions.Breadth_first_Search_class import *
from solutions.two_pointers_class import *
from solutions.math_class import *
from solutions.hash_table_class import *

from testcodes.array_test_functions import *
from testcodes.string_test_functions import *
from testcodes.dynamic_programming_test_functions import *
from testcodes.Depth_first_Search_class_test_functions import *
from testcodes.Breadth_first_Search_class_test_functions import *
from testcodes.two_pointers_class_test import *
from testcodes.math_class_test import *
from testcodes.hash_table_test_functions import *

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
	
def breadth_first_search_test(solution, test_solution):
	test_solution.test_minDepth(solution)
	test_solution.test_levelOrderBottom(solution)
	test_solution.test_levelOrder(solution)
	test_solution.test_zigzagLevelOrder(solution)
	test_solution.test_solve(solution)

def two_pointers_test(solution, test_solution):
	test_solution.test_threesum(solution)
	test_solution.test_threeSumClosest(solution)
	test_solution.test_foursum(solution)
	test_solution.test_sortColors(solution)
	test_solution.test_removeDuplicates(solution)
	test_solution.test_removeDuplicates_part(solution)

def math_test(solution, test_solution):
	test_solution.test_mySqrt(solution)
	test_solution.test_isPowerOfTwo(solution)
	test_solution.test_isUgly(solution)
	test_solution.test_isPerfectSquare(solution)
	test_solution.test_maxRotateFunction(solution)
	test_solution.test_integerReplacement(solution)
	test_solution.test_minMoves2(solution)

def hash_table_test(solution, test_solution):
	test_solution.test_singleNumber(solution)
	test_solution.test_findRepeatedDnaSequences(solution)
	test_solution.test_isAnagram(solution)
	test_solution.test_getHint(solution)
	test_solution.test_fourSumCount(solution)

def main():
	#array_test(Array(),Array_Test_func())
	#string_test(String(),String_Test_func())
	#dynamic_programming_test(dynamic_programming(),Dynamic_Programming_Test_func())
	#depth_first_search_test(Depth_first_Search(),Depth_first_Search_Test_func())
	#breadth_first_search_test(Breadth_first_Search(),Breadth_first_Search_Test_func())
	#two_pointers_test(two_pointers(),two_pointer_class_Test_func())
	#math_test(math(),math_class_Test_func())
	hash_table_test(hash_table(), hash_table_class_Test_func())	
if __name__ == '__main__':
	main()

