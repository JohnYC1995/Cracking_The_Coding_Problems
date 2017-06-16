#!/usr/bin/python
# -*- coding: utf-8 -*-
# This is main function for CCI questions
# author Yongjun Chen

from functions import * 
from test_functions import *

def main():
	solution = Solution()
	test_solution = Test_Solution()
	test_solution.test_isunique(solution)
	test_solution.test_check_permutation(solution)
	test_solution.test_URLify(solution)
	test_solution.test_One_Away(solution)
	test_solution.test_String_Compression(solution)
	test_solution.test_Rotate_Matrix(solution)
	test_solution.test_Zero_Matrix(solution)
	test_solution.test_Single_linkedlist(solution)
	test_solution.test_sum_lists_backward_type(solution)
	test_solution.test_sum_lists_forward_type(solution)
	test_solution.test_palindrome_check(solution)
	test_solution.test_Mystack(solution)
	test_solution.test_SetofStack(solution)
	test_solution.test_myqueue(solution)
	test_solution.test_sort_stack(solution)
	test_solution.test_Animal_Shelter(solution)
	test_solution.test_tree(solution)
	test_solution.test_graph()
	test_solution.test_minal_tree(solution)
	test_solution.test_insertion(solution)
	test_solution.test_Int2Binary(solution)
	test_solution.test_flip_bit_to_win(solution)
	test_solution.test_next_number(solution)
	test_solution.test_conversion(solution)
	test_solution.test_swapOddEvenBits(solution)
	test_solution.test_check_prime(solution)
	test_solution.test_sieveOfEratosthenes(solution)
	test_solution.test_fibonacci_2(solution)
	test_solution.test_Triple_Step(solution)
	test_solution.test_Robot_in_a_Grid(solution)
	test_solution.test_Magic_Index(solution)
	test_solution.test_Recursive_Multiply(solution)
	test_solution.test_Permutations(solution)
	test_solution.test_Coins(solution)
	test_solution.test_Bubble_sort(solution)
	test_solution.test_Selection_sort(solution)
	test_solution.test_Merge_sort(solution)
	test_solution.test_Sorted_Merge(solution)
	test_solution.test_SortedSearchNoSize(solution)
if __name__ == '__main__':
	main()


