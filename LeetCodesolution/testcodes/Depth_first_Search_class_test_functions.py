'''
!/usr/bin/python
 -*- coding: utf-8 -*-
 This is depth first search test function for Leetcode questions
 @ author Yongjun Chen
LeetCode
'''
from Depth_first_Search_class import * 
from TreeNode import *
#Test function
class Depth_first_Search_Test_func(object):
	def __init__(self):
		self.index = 1
	def pname(self, name):
		result = '==================DFS '+str(self.index)+ '.' + str(name)  + '=================='
		print(result)

	def sresult(self, name, *args):
		self.pname(name)
		self.index += 1
		print(args)

	def test_isSameTree(self, solution):
		lefttree = TreeNode(4)
		righttree = TreeNode(5)
		ptree = TreeNode(3)
		ptree.left = lefttree
		ptree.right = righttree
		qtree = TreeNode(3)
		qtree.left = lefttree
		qtree.right = righttree
		self.sresult("isSameTree - easy",solution.isSameTree(ptree,qtree))

	def test_isSymmetric(self,solution):
		lefttree = TreeNode(4)
		righttree = TreeNode(4)
		ptree = TreeNode(3)
		ptree.left = lefttree
		ptree.right = righttree
		self.sresult("isSymmetric - easy", solution.isSymmetric(ptree))

	def test_maxDepth(self,solution):
		le2lefttree = TreeNode(4)
		lefttree = TreeNode(10)
		lefttree.left = le2lefttree
		righttree = TreeNode(4)
		ptree = TreeNode(3)
		ptree.left = lefttree
		ptree.right = righttree
		self.sresult("maxDepth - easy", solution.maxDepth(ptree))

	def test_sortedArrayToBST(self,solution):
		array = [5,4,3,2,1,2,3,4,5]
		self.sresult("sortedArrayToBST - easy", solution.sortedArrayToBST(array))



