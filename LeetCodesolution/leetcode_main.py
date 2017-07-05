#LeetCode
from functions import * 
from test_functions import *
import pdb
def main():
	solution = Solution()
	test_solution = Test_Solution()
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
if __name__ == '__main__':
	main()

