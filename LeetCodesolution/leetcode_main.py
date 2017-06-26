#LeetCode
from functions import * 
from test_functions import *
import pdb
def main():
	solution = Solution()
	test_solution = Test_Solution()
	test_solution.test_twoSum(solution)
	test_solution.test_lengthOfLongestSubstring(solution)
	test_solution.test_findLongestWord(solution)
	test_solution.test_intersection(solution)
	test_solution.test_largestnumber(solution)
	test_solution.test_two_pointers(solution)

if __name__ == '__main__':
	main()

