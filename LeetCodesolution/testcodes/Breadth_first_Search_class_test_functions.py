'''
!/usr/bin/python
 -*- coding: utf-8 -*-
 This is breadth first search test function for Leetcode questions
 @ author Yongjun Chen
LeetCode
'''
from Depth_first_Search_class import * 
from TreeNode import *
#Test function
# example tree
le2lefttree = TreeNode(4)
lefttree = TreeNode(10)
lefttree.left = le2lefttree
righttree = TreeNode(4)
ptree = TreeNode(3)
ptree.left = lefttree
ptree.right = righttree
class Breadth_first_Search_Test_func(object):
	def __init__(self):
		self.index = 1
	def pname(self, name):
		result = '==================DFS '+str(self.index)+ '.' + str(name)  + '=================='
		print(result)

	def sresult(self, name, *args):
		self.pname(name)
		self.index += 1
		print(args)
    #--------- easy ----------#
	def test_minDepth(self, solution):
		le2lefttree = TreeNode(4)
		lefttree = TreeNode(10)
		lefttree.left = le2lefttree
		righttree = TreeNode(4)
		ptree = TreeNode(3)
		ptree.left = lefttree
		ptree.right = righttree		
		self.sresult("minDepth - easy ", solution.minDepth(ptree))

	def test_levelOrderBottom(self, solution):
		self.sresult("levelOrderbottom - easy ", solution.levelOrderBottom(ptree))		

	#---------Medium----------#
	def test_levelOrder(self, solution):
		self.sresult("levelOrder - medium ", solution.levelOrder(ptree))

	def test_zigzagLevelOrder(self, solution):
		self.sresult("zigzagLevelOrder - medium ", solution.zigzagLevelOrder(ptree))

	def test_solve(self, solution):
		matrix = [['X','X','X','X'],['X','O','O','X'],['X','X','O','X'],['X','O','X','X']]  
		self.sresult("solve - medium ", solution.solve(matrix))

