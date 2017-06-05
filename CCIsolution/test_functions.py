#!/usr/bin/python
# -*- coding: utf-8 -*-
# This is test function class for CCI solutions
# author Yongjun Chen
from functions import *
from SingleList import *
from Graph import *
import inspect
import sys  


#Test function
class Test_Solution(Solution):

	def __init__(self):
		pass
	def pname(self,name):
		result = '==================' + str(name) + '=================='
		print(result)
	def sresult(self,name,*args):
		self.pname(name)
		print(args)
	#1.1 Is Unique
	def test_isunique(self,solution):
		string = "1242"
		self.sresult("1.1 test_isunique:",solution.Is_unique(string))
	#1.2 Check Permutation
	def test_check_permutation(self, solution):
		string1 = '12345678'
		string2 = '87654321'
		self.sresult("1.2 test_check_permutation:",\
			solution.Check_Permutation(string1,string2))
	#1.3
	def test_URLify(self, solution):
		string = 'Mr John Smith'
		self.sresult("1.3 test_URLify:",solution.URLify(string))
	#1.5
	def test_One_Away(self,solution):
		string1 = 'pale'
		string2 = 'bake'
		self.sresult("1.5 test_One_Away:",solution.One_Away(string1,string2))
	#1.6
	def test_String_Compression(self,solution):
		string = 'aabbbbbcdddcccceccd'
		self.sresult("1.6 test_String_Compression:",solution.String_Compression(string))
	#1.7 
	def test_Rotate_Matrix(self,solution):
		matrix = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
		self.sresult("1.7 test_Rotate_Matrix:",solution.Rotate_Matrix(matrix))
	#1.8
	def test_Zero_Matrix(self,solution):
		matrix = np.array([[1,1,1],[1,1,0],[1,1,1]])
		self.sresult("1.8 test_Zero_Matrix:",solution.Zero_Matrix(matrix))
	#---------Linked List----------#
	#2.1-2.4
	def test_Single_linkedlist(self,solution):
		self.pname("2.1-2.14 test_Single_linkedlist:")
		solution.Single_linkedlist()

	#2.5
	def test_sum_lists_backward_type(self,solution):
		self.pname("2.5 test_sum_lists_backward_type:")
		l1 = LinkList()
		l2 = LinkList()
		l1.initlist([7,1,6])
		l2.initlist([5,9,2])
		result = solution.sum_lists(l1,l2,'backward')
		for index in range(result.getlength()):
			print(result.getitem(index))
	#2.5 extend
	def test_sum_lists_forward_type(self,solution):
		self.pname("2.5 test_sum_lists_forward_type:")
		l1 = LinkList()
		l2 = LinkList()
		l1.initlist([7,1,6])
		l2.initlist([5,9,2])
		result = solution.sum_lists(l1,l2,'forward')
		for index in range(result.getlength()):
			print(result.getitem(index))
	#2.6 
	def test_palindrome_check(self,solution):
		l = LinkList()
		l.initlist([1,2,3,3,2,2])
		self.sresult("2.6 test_palindrome_check:",solution.Palindrome_check(l))
	#3.2
	def test_Mystack(self,solution):
		self.pname("3.2 test_Mystack")
		solution.Mystack()
	#3.3 
	def test_SetofStack(self,solution):
		self.pname("3.3 test_SetofStack")
		solution.SetofStack()
	#3.4
	def test_myqueue(self,solution):
		self.pname("3.4 test_myqueue")
		solution.myqueue()
	#3.5
	def test_sort_stack(self,solution):
		self.pname("3.5 test_sort_stack")
		solution.sort_stack()
	#3.6
	def test_Animal_Shelter(self,solution):
		self.pname("3.6 test_Animal_Shelter")
		solution.Animal_Shelter()
	#4-1 Tree
	def test_tree(self,solution):
		self.pname("4.1 test tree")
		testvalue = range(10)
		solution.Binary_Tree(testvalue)
	#4-2 Graph
	def test_graph(self):
		self.pname("test graph")
		a_graph= Graph()
		a_graph.add_node_lists(['a','b','c','d','e'])
		a_graph.add_edge(('a','b'))
		a_graph.add_edge(('a','c'))
		a_graph.add_edge(('b','d'))
		a_graph.add_edge(('b','e'))
		a_graph.do_deep_first_search('a')
		a_graph.do_bread_first_search('a')
		a_graph.show_graph()
	#4.2 minial tree
	def test_minal_tree(self,solution):
		test_list = [1,2,3,4,5,6,7]
		self.sresult("4.2 test_minal_tree",solution.list2minimal_tree(test_list))
	#4.3 List of Depths:


	#5.1 Insertion
	def test_insertion(self,solution):
		binary1 = bin(0b10000000000)
		binary2 = bin(0b10011)
		i = 2
		j = 6
		self.sresult("5.1 Insertion",solution.Insertion(binary1,binary2,i,j))
	#5.2 Int2Binary
	def test_Int2Binary(self,solution):
		interg1 = 0.5
		interg2 = 0.75
		result1 = solution.Int2Binary(interg1)
		result2 = solution.Int2Binary(interg2)
		self.sresult("5.2 Int2Binary",\
					solution.Int2Binary(interg1),\
			        solution.Int2Binary(interg2))
	#5.3 Flip Bit to Win	
	def test_flip_bit_to_win(self,solution):
		input_bit = 0b10011
		self.sresult("5.3 Flip Bit to Win",solution.flip_bit_to_win(input_bit))
	#5.4next_number
	def test_next_number(self,solution):
		test = 0b1001000
		self.sresult("5.4 Next number",solution.next_number(test))
	#5.6Conversion
	def test_conversion(self,solution):
		number1 = 0b1001110
		number2 = 0b0001111
		self.sresult("5.6 Conversion",solution.Conversion(number1,number2))
	#5.7swapOddEvenBits
	def test_swapOddEvenBits(self,solution):
		interg = 0b010101010
		self.sresult("5.7 swapOddEvenBits",bin(solution.swapOddEvenBits(interg)))
	#-------Math and Logic Puzzles-------#
	def test_check_prime(self,solution):
		number = int(13)
		self.sresult("check_prime",solution.check_prime(number))



