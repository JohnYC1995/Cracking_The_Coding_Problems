#!/usr/bin/python
# -*- coding: utf-8 -*-
# This is function class for CCI questions
# author Yongjun Chen
import numpy as np
from SingleList import *
from Mystack import *
from SetofStack import *
from Myqueue import *
from Animal_shelter import *
from Tree import *
from Graph import *
import random
import math
import string  
from random import randint

debug = True

class Solution(object):
	
	def __init__(self):
		self.test_dict = {}
	#-------Array and Lists--------#
	#Hash table can be implemented by a Linked list and a Hash code function
	#Lookup time B:O(N); W"O(1)

	#1.1 Is Unique
	def Is_unique(self,string):
		dic = set()
		for s in string:
			if s in dic:
				return False
			else:
				dic.add(s)
		return True
	#1.2 Check Permutation
	def Check_Permutation(self, string1, string2):
		if len(string1) != len(string2):
			return False
		else:
			for index in range(len(string1)):
				if string1[index] != string2[len(string2)-index-1]:
					return False
			return True	
	#1.3 URLify
	def URLify(self,string):
		result = ''
		for item in string:
			if item == ' ':
				result = result + '20%'
			else:
				result = result + item
		return result
	#1.5 One Away
	def One_Away(self,string1,string2):
		count =0
		#insert 
		if len(string1) == len(string2)-1:
			for item in range(len(string1)):
				if string1[item] != string2[item]:
					if string1[item] != string2[item+1]:
						return False
			return True
		#replace
		elif len(string1) == len(string2):
			for item in range(len(string1)):
				if string1[item] != string2[item]:
					count += 1
				if count >1:
					return False
			return True
		#remove
		elif len(string1) ==len(string2)+1:
			for item in range(len(string2)):
				if string1[item] != string2[item]:
					if string1[item+1] != string2[item]:
						return False
			return True
		else:
			return False
	#1.6 String Compression
	def String_Compression(self, string):
		count = 1
		result = ''
		for item in range(len(string)-1):
			#print("item",item)
			#special case: last two elements
			if (string[item+1] == string[item]) and ((item+1) != (len(string)-1)):
				count += 1
			elif string[item+1] == string[item]:
				result = result + string[item] + str(count+1)
			elif string[item+1] != string[item] and ((item+1) != (len(string)-1)):
				result = result + string[item] + str(count)
				count = 1
			else:
				result = result + string[item] + str(count)+string[item+1]+str(1)
		if len(result) > len(string):
			return string
		else:
			return result
	#1.7 Rotate Matrix O(H*W)
	def Rotate_Matrix(self, matrix):
		H = matrix.shape[0]
		W = matrix.shape[1]
		result = np.zeros((W,H))
		for h in range(W):
			for w in range(H):
				result[h][w] = matrix[H-w-1][h]
		return result
	#1.8 Zero Matrix O(H*W)
	def Zero_Matrix(self,matrix):
		result = np.zeros((matrix.shape[0],matrix.shape[1]))
		zero_list = []
		for i in range(matrix.shape[0]):
			for j in range(matrix.shape[1]):
				result[i][j] = matrix[i][j]
				if matrix[i][j] == 0:
						zero_list.append((i,j))
		for item in zero_list:
			for i in range(matrix.shape[0]):
				result[i][item[1]] = 0
			for i in range(matrix.shape[1]):
				result[item[0]][i]= 0
		return result
	#1.9 String Rotation xy always be sub of yxyx
	def String_Rotation(self, string1,string2):
	#check whether string2 is a substring of string1+string1 or not
		pass
	#---------Linked List----------#
	# Ad: can add and remove the elements from the beginning of the list in O(1)
	#
	def Single_linkedlist(self):
		l = LinkList()
		linkedlist = l.initlist([1,2,3,3,4,5])
		l.remove_dup()
		#2.1
		print("2.1 remove_dup:")
		print(l.getlength())
		#2.2
		print("2.2 ktoend:")
		print(l.Return_Kth_to_Last(2))
		#2.3
		l.Delete_middle_node(2)
		print("2.3 delete_middle:")
		print(l.getlength())
	#2.5
	def sum_lists(self,list1,list2,type_of_sum='backward'):
		list1_use = ''
		list2_use = ''
		l = LinkList()
		result = []
		for index in range(list1.getlength()):
			list1_use = list1_use + str(list1.getitem(list1.getlength() - index - 1))
		for index in range(list2.getlength()):
			list2_use = list2_use + str(list2.getitem(list2.getlength() - index - 1))
		sum_result = str(int(list1_use)+int(list2_use))
		for i in range(len(sum_result)):
			if type_of_sum == 'backward':
				result.append(sum_result[len(sum_result)-i-1])
			elif type_of_sum == 'forward':
				result.append(sum_result[i])
			else:
				print('illegal type of sum')
				return
		l.initlist(result)
		return l
	#2.6Palindrome
	def Palindrome_check(self,list):
		for index in range(list.getlength()):
			if list.getitem(index) != list.getitem(list.getlength()-index-1):
				return False 
		return True
	#---------Stack and Queue------#
	# Ad: can add and remove the elements within O(1)
	# disad: cannot access ith elements within O(1)
	# Often be used in Recursive alggorithms
	#3.1
	# seperate teh whole stack into three parts. for each part, use for each stack.
	#3.2
	def Mystack(self):
		mystack = Mystack()
		mystack.push(1)
		mystack.push(2)
		mystack.push(6)
		mystack.push(0)
		mystack.pop()
		mystack.pop()
		mystack.pop()	
		mystack.show_stack()
		print(mystack.get_min())
	#3.3
	def SetofStack(self):
		mysetofstack = SetofStack(5)
		mysetofstack.push(1)
		mysetofstack.push(2)		
		mysetofstack.push(3)
		mysetofstack.push(4)
		mysetofstack.pop()
		mysetofstack.pop()
		mysetofstack.show_setofstack()
	#3.4
	def myqueue(self):
		myqueue = Myqueue()
		myqueue.push(1)
		myqueue.push(2)
		myqueue.push(3)
		myqueue.push(4)
		myqueue.push(5)
		print(myqueue.pop())
		print(myqueue.pop())
		print(myqueue.pop())
		print(myqueue.pop())
	#3.5
	def sort_stack(self):
		stack1 = Mystack()
		stack1.push(1)
		stack1.push(2)
		stack1.push(4)
		stack1.push(6)
		stack1.push(3)
		stack2 = Mystack()
		stack3 = Mystack()
		nums = stack1.size()
		for i in range(nums):
			temp = stack1.get_min()
			while stack1.isEmpty() == False:
				if stack1.peek() == temp:
					stack1.pop()
				else:
					a = stack1.pop()
					stack2.push(a)
			while stack2.isEmpty() == False:
				stack1.push(stack2.pop())
			stack3.push(temp)
		stack3.show_stack()
	#3.6 Animal_Shelter
	def Animal_Shelter(self):
		a_shelter = Animal_Shelter()
		a_shelter.enqueue(('sunny','cat'))
		a_shelter.enqueue(('cathy','cat'))
		a_shelter.enqueue(('disc','dog'))
		a_shelter.show_animals()
		print(a_shelter.dequeueDog())
		a_shelter.show_animals()
		a_shelter.enqueue(('catlin','dog'))
	#--------- Trees and Graphs --------#
	#Nonlinear data structures
	#More efficient when doing the search
	#Binary tree Traversal
	def Binary_Tree(self,testdata):
		tree = Tree()
		for elem in testdata:                  
			tree.add_item(elem)
		print("=====R_In_order_Traversal=====")
		tree.R_In_order_Traversal(tree.root)
		print(tree.iresult)
		print("=====R_Pre_order_Traversal=====")
		tree.R_Pre_order_Traversal(tree.root)
		print(tree.presult)
		print("=====R_Pose_order_Traversal=====")
		tree.R_Pose_order_Traversal(tree.root)
		print(tree.poresult)
		print("=====S_In_order_Traversal=====")
		tree.S_In_order_Traversal(tree.root)
		print("=====S_Pre_order_Traversal=====")
		tree.S_Pre_order_Traversal(tree.root)
		print("=====S_Post_order_Traversal=====")
		tree.S_Post_order_Traversal(tree.root)
	#Graph
	def Graph(self):
		a_graph= Graph()
		a_graph.add_node_lists(['a','b','c','d','e'])
		a_graph.add_edge(('a','b'))
		a_graph.add_edge(('a','c'))
		a_graph.add_edge(('b','d'))
		a_graph.add_edge(('b','e'))
		a_graph.do_deep_first_search('a')
		a_graph.do_bread_first_search('a')
		a_graph.show_graph()
	#4.2 Minimal Tree 
	def list2minimal_tree(self,sortedlist):
		tree = Tree()
		for elem in sortedlist:                  
			tree.add_item(elem)
		tree.R_In_order_Traversal(tree.root)
		return tree.iresult
		l = LinkList()
		linkedlist = l.initlist([1,2,3,3,4,5])
		l.remove_dup()
		#2.1
		print("2.1 remove_dup:")
		print(l.getlength())
		#2.2
		print("2.2 ktoend:")
		print(l.Return_Kth_to_Last(2))
		#2.3
		l.Delete_middle_node(2)
		print("2.3 delete_middle:")
		print(l.getlength())
	#4.3 list_of_depths
	def list_of_depths(self,atree):
		listoftree = atree.get_tree_element()
		listoflink = []
		listoflink.append(LinkList())
		count = 1
		for index in range(len(listoftree)):
			if index == count:
				count += count + 1 
	#--------- Bit Manipulation ----------#
	#5.1 Insertion
	def Insertion(self,binary1,binary2,i,j):
		_,binary1 = str(binary1).split('b',1)
		_,binary2 = str(binary2).split('b',1)
		for index in range(len(binary1)):
			if (index>=len(binary1)-j-1) and (index <=len(binary1)-i-1):
				binary1 = binary1[:index] + binary2[index-(len(binary1)-j-1)] + binary1[index+1:]
		return binary1
	#5.2 Binary to String
	def Int2Binary(self,Interg):
		result = ''
		if Interg == 1.0:
			result='1.0'
		elif Interg ==0.0:
			result='0.0'
		else:
			while Interg != 1.0:
				Interg = Interg*2
				result += str(int(Interg)) 
				if (Interg!=int(Interg)) and (int(Interg)== 1.0):
					Interg = Interg - int(Interg)
			result= '0.'+result
		return result
	#5.3
	def flip_bit_to_win(self,input_bit):
		input_bit = bin(input_bit)
		_,input_bit = str(input_bit).split('b',1)
		zero_index = []
		for index in range(len(input_bit)):#O(b)
			if input_bit[index] == '0':
				zero_index.append(index)
		max_bit = 0
		for index in range(len(zero_index)):#O(z)<O(b)
			if index == (len(zero_index)-1) == 0:
				sub_bit = input_bit[:zero_index[0]]+'1'+input_bit[zero_index[0]+1:]
			elif index == 0:
				sub_bit = input_bit[:zero_index[0]]+'1'+input_bit[zero_index[0]+1:zero_index[1]]
			elif index == len(zero_index)-1:
				sub_bit = input_bit[zero_index[-2]+1:zero_index[-1]] + '1'+ input_bit[zero_index[-1]+1:]
			else:
				sub_bit = input_bit[zero_index[index-1]+1:zero_index[index]] + '1' +input_bit[zero_index[index]+1:zero_index[index+1]]
			if len(sub_bit) > max_bit:
				max_bit = len(sub_bit)
		return max_bit
	#5.4 Next Number:
	def next_number(self,numbers):
		numbers = bin(numbers)
		_,numbers = str(numbers).split('b',1)
		zero_nums = 0;zeros = '';ones = ''
		for index in range(len(numbers)):#O(b)
			ones += '1'
			if numbers[index] == '0': 
				zero_nums += 1;zeros += '0'
		if zero_nums == 0:
			return numbers,numbers
		else:
			smallest = zeros + ones[zero_nums:]
			largest  = ones[:len(numbers)-zero_nums]+zeros
		return smallest,largest
	#5.5
	#Check whether it's power of 2 or not
	#5.6 Conversion:
	def Conversion(self,numbers,numbers1):
		numbers = bin(numbers)
		numbers1 = bin(numbers1)
		_,numbers = str(numbers).split('b',1)
		zero_index = []
		if numbers == numbers1:
			print("no need to flip")
			return
		else:
			for index in range(len(numbers)):#O(b)
				if numbers[index] == '0':
					zero_index.append(index)
		return zero_index
	#5.7swapOddEvenBits
	def swapOddEvenBits(self,interg):
		return (((interg & 0xaaaaaaaa) >> 1) | ((interg & 0x55555555) << 1))
	#-------6. Math and Logic Puzzles-------#
	#Not often been asked since lots of companies have polices to ban them. But still could be. 
	def check_prime(self,number):
		if number < 2:
			return False
		else:
			for num in range(2,int(number**0.5)):
				if (number%num) == 0:
					return False
			return True
	# Get prime KEY: If it's prime, it will not be divided by the smaller one.
	def cut_off(self,prime):
		for index in range(len(self.flag)):
			if index % prime  == 0 and index != prime:
				self.flag[index] = False

	def get_next_prime(self,prime):
		next_prime = prime + 1 
		while (next_prime < len(self.flag)) and self.flag[next_prime] == False:
			next_prime += 1
		return next_prime

	def sieveOfEratosthenes(self,max_number):
		self.flag = [True for i in range(max_number)]
		prime = 2
		while prime <= int(max_number**0.5):
			self.cut_off(prime)
			prime = self.get_next_prime(prime)
		self.flag[0] = False
		return self.flag

	#----------7 Object-Oriented Design----------#

	#----------8 Recursion and Dynamic Programming---------#
	# O(2^n)
	def fibonacci_1(self,number):
		if number == 0:
			return 0
		elif number == 1:
			return 1
		else:
			return fibonacci(number-1) + fibonacci(number-2)
	# O(n)
	def fibonacci_2(self,number):
		if number == 0:
			return 0
		a = 0
		b = 1
		for index in range(number):
			c = a + b 
			a = b
			b = c
		return a + b
	#8.1 
	def Triple_Step(self,steps):
		result = 0
		for j in range(int(steps/2)):
			for i in range(steps):
				if (steps - 2 * j - 3 * i) >= 0 and (steps - 2 * j - 3 * i) <= steps:
					result += 1
		return result
	#8.2 
	def Robot_in_a_Grid(self,R,C):
		R_list = ['>']*R
		C_list = ['v']*C
		Policy = {0:R_list,1:C_list}
		result = []
		for i in range(R+C):
			index = random.randint(0,1)
			if len(Policy[index]) == 0:
				index = abs(1-index)
			cur_policy = Policy[index].pop()
			result.append(cur_policy)
		return result
	#8.3
	def Magic_Index(self,an_array):
		result = []
		for i in range(len(an_array)):
			if (i+1) == an_array[i]:
				result.append(i+1)
		if len(result) == 0:
			print("No magic array")
			return 
		else:
			return result
	#8.5
	def Recursive_Multiply(self,A,B):
		if A - B >0:
			multi = B
			base = A
		else:
			multi = A
			base = B
		result = 0
		for i in range(multi):
			result += base
		return result
	#8.7
	def Permutations_fuc(self,string):
		return string[:-1]+string[-1],string[-1]+string[:-1]
	def Permutations(self,string):
		temp_result = []
		if len(string) == 1:
			return string
		else:
			temp_result.append(string[:2])
			for index in range(1,len(string)-1):
				for i in range(math.factorial(index)):
					a,b = self.Permutations_fuc(temp_result.pop(0))
					temp_result.append(a+string[index+1])
					temp_result.append(b+string[index+1])
			last_range = len(temp_result)
			for i in range(math.factorial(last_range)):
				a,b = self.Permutations_fuc(temp_result.pop(0))
				temp_result.append(a)
				temp_result.append(b)
		return temp_result
	#8.11
	def Coins(self,N):
		return 4**N
	#---------9. System Design and Scalability--------#

	#---------10. Sorting and Searching---------#
	##Classic sort:
	#-Bubble sort:O(n^2)
	def Bubble_sort(self,data):
		lenth = len(data)-1
		for i in range(len(data)):
			for index in range(lenth):
				if data[index]>data[index+1]:
					temp = data[index]
					data[index] = data[index+1]
					data[index+1] = temp
			lenth -= 1
		return data
	#-Selection sort:O(n^2)
	def Selection_sort(self,data):
		#searching
		result = []
		lenth = len(data)
		for index in range(lenth):
			min_index = 0;min_value = data[0]
			for i in range(len(data)):
				if data[i]<min_value:
					min_value = data[i];min_index = i
			result.append(data.pop(min_index))
		return result
	#-Merge sort
	def mergeSort(self,alist):
	    if len(alist)>1:
	        mid = len(alist)//2
	        lefthalf = alist[:mid]
	        righthalf = alist[mid:]
	        self.mergeSort(lefthalf)
	        self.mergeSort(righthalf)
	        i=0
	        j=0
	        k=0
	        while i < len(lefthalf) and j < len(righthalf):
	            if lefthalf[i] < righthalf[j]:
	                alist[k]=lefthalf[i]
	                i=i+1
	            else:
	                alist[k]=righthalf[j]
	                j=j+1
	            k=k+1
	        while i < len(lefthalf):
	            alist[k]=lefthalf[i]
	            i=i+1
	            k=k+1

	        while j < len(righthalf):
	            alist[k]=righthalf[j]
	            j=j+1
	            k=k+1
	    return alist
	#-Quick sort
	def quick_sort(self,mylist,start,end):
		pivot = self.partition(mylist,start,end)
		quick_sort(mylist,start,pivot-1)
		quick_sort(mylist,pivot+1, end)
		return mylist
	#-Radix sort
	#Sorted Merge
	def Sorted_Merge(self,lista,listb):
		result = [0]*(len(lista)+len(listb))
		i = len(lista)
		j = len(listb)
		k = i + j - 1
		while k >= 0:
			if (lista[i-1]>listb[j-1]) or (j<=0):
				result[k] = lista[i-1]
				i -= 1
				k -= 1
			else:
				result[k] = listb[j-1]
				j -= 1
				k -= 1
		return result
	# 10.3 Sorted Search, No Size
	def SortedSearchNoSize(self,Listy,item):
		diction = {}
		index   = 0
		while True:
			diction[Listy.elementAt(index)] = diction.get(Listy.elementAt(index),'start:') + str(index) + '  ' 
			index += 1
			if Listy.elementAt(index) == -1:
				break
		if item not in diction.keys():
			print("No such item")
			return 
		else:
			return diction[item]

	#------------12. C and C++ -----------#
	'''
	1. Virtual Function: used to inheriented by child;when we can't (or don't want to) implement a method for the parent
	class.
	2. Pointers and References
		2.1 Pointers '*'
		- When define variable using *, it shows that this variable is a pointer.
		- When '*' is used before the pointer variable, it means get the value of this pointer. 
		- Example
			int a = 1000
			int * b = &a  // b is a pointer
			print b  // show a's memory location
			print *b  // show the value in a's memory location, 1000
		2.2 Reference '&'
		- When define variable using &, it means this variable is the reference of the 
			variable if refered.
		  namely, its another name of the refered variable.
		- When '&' is used before the variable, it means get the location of this variable.
		- Example
			int a = 1000
			int &c = a
			print a //print 1000
			print c //print 1000 since c is just another name of a
			print &a // print a's location
			print &c // print c's location, since c is reference of a, so the location of c
			is the same if a.
	'''
	#------------13. JAVA ------------#
	'''
	1.Overloading vs. Overriding
	1.1 Overloading
		When two methods have the same name but different in the type or number of arguments.
	1.2 Overriding
		When a method shares the same name and function signature as another method in its 
		supper class.
	'''
	#------------14. Databases--------#
	'''
	Not go into this part yet.
	'''
	#------------15. Threads and locks-------#
	'''
	It's about multithreading programming, I am not go into this part yet.
	'''
	#------------Moderate-------------#
	#16.1 Number Swapper
	def swapper(self, a, b):
		a = a - b 
		b = b + a 
		a = b - a
		return a, b
	#16.2 Word Frequencies
	def Word_Frequencies(self, testbook, givenword):
		givenword = str(givenword)
		if not self.test_dict:
			delete_character = string.punctuation
			for word in testbook:
				if word in delete_character:
					testbook = testbook.replace(word, ' ')
			testbook = testbook.split(' ')
			for word in testbook:			
				self.test_dict[word] = self.test_dict.get(word,0) + 1
		if givenword not in self.test_dict.keys():
			print("the word is not in the book")
			return 
		else:
			return self.test_dict[givenword]
	#16.6 Smallest Difference
	def Smallest_Difference(self,list1,list2):
		list1.sort()
		list2.sort()
		print(list1)
		i = 0
		j = 0
		difference = abs(list1[0]-list2[0])
		while i < len(list1) and j < len(list2):
			if abs(list1[i]-list2[j]) < difference:
				location   = []
				location.append((list1[i],list2[j]))
				difference = abs(list1[i]-list2[j])
				print(difference)
				print(list1[i],list2[j])
				print(i,j)
			if list1[i] < list2[j]:
				i += 1
			else: 
				j += 1
		return difference, location
	#16.16 Sub Sort
	def sub_sort(self,tlist):
		leftlist = [tlist[0]]
		rightlist = [tlist[-1]]
		countleft = True
		countright = True
		for i in range(len(tlist)-1):
			if countleft and tlist[i+1]>leftlist[i]:
				leftlist.append(tlist[i+1])
				leftindex = i + 2
			if countright and tlist[-(i+2)] < rightlist[-1]:
				rightlist.append(tlist[-(i+2)])
				rightindex = len(tlist)-i-1
			if tlist[i+1] < tlist[i]:
				countleft = False
			if tlist[-(i+2)] > rightlist[-1]:
				countright = False
			minvalue = tlist[leftindex]
			maxvalue = tlist[leftindex]
			if i >= leftindex and i <= rightindex:
				if tlist[i] <  minvalue:
					minvalue = tlist[i] 
				if tlist[i] > maxvalue:
					maxvalue = tlist[i]
		while leftlist[-1] > minvalue:
			leftlist.pop()
		while rightlist[-1] <maxvalue:
			rightlist.pop()
		return (len(leftlist),len(tlist)-len(rightlist))
	#16.17 Contiguous Sequence
	def contiguous_sequence(self,testlist):
		maxvalue = testlist[0] + testlist[1]
		for index in range(len(testlist)):
			if index == 0:
				tempvalue = testlist[index] + testlist[index+1]
			elif index == len(testlist)-1:
				tempvalue = testlist[index-1] + testlist[index]
			else:
				tempvalue = testlist[index-1] + testlist[index] + testlist[index+1]
			if tempvalue > maxvalue:
				maxvalue = tempvalue
		return maxvalue
	#16.21 sum_swap
	def sum_swap(self,list1,list2):
		#sum list
		sumlist1 = 0
		sumlist2 = 0
		for i in range(len(list1)):
			sumlist1 += list1[i]
		for i in range(len(list2)):
			sumlist2 += list2[i]
		target = (sumlist1-sumlist2)/2
		list2set = set(list2)
		flag = False
		for item in list1:
			if (item - target) in list2set:
				return (item, int((item - target)))
				flag = True
		if flag == False:
			print("the lists cannot be the same")
			return
	# 16.22 rand7fromrand5
	def rand7fromrand5(self):
		while True:
			seed = 5*randint(0,5)+randint(0,5)
			if seed < 21:
				return seed % 7


if __name__ == '__main__':
	item = (1,2)
	s = Solution()
	test = 0b1001
	alist = s.Bubble_sort([111,2,3,4,5,13])
	blist = s.Bubble_sort([6,7,8,9,10,11])
	#alist = s.Sorted_Merge(alist,blist)
	book  = 'we are the friends, but we are not always be friendly with each other.'
	num   = s.Word_Frequencies(book, 'friends')
	num2  = s.Word_Frequencies(book, 'we')
	dif,loca = s.Smallest_Difference(alist,blist)
	print(dif,loca)
	a = [2,3,4,1,34,3,4,4]
	b = [2,3,4,1,34,3,4,5]
	result = s.sum_swap(a,b)
	print(result)
	print(s.rand7fromrand5())
