#!/usr/bin/python
# -*- coding: utf-8 -*-
# This is a tree class
# author Yongjun Chen

from TreeNode import *


class Tree(object):
	
	def __init__(self):
		self.root = Node()
		self.Myqueue = []
		self.iresult = []
		self.presult = []
		self.poresult =[]
		self.listofitem = []

	def add_item(self,item):
		node = Node(item)
		self.listofitem.append(node.elem)
		if self.root.elem == -1:
			self.root = node
			self.Myqueue.append(self.root)
		else:
			treeNode = self.Myqueue[0] 
			if treeNode.lchild == None:
				treeNode.lchild = node
				self.Myqueue.append(treeNode.lchild)
			else:
				treeNode.rchild = node
				self.Myqueue.append(treeNode.rchild)
				self.Myqueue.pop(0)
	def get_tree_element(self):
		return self.listofitem
	#---- Traversal: Recursive version -----#
	#In order
	def R_In_order_Traversal(self,root):
		if root == None:
			return
		self.iresult.append(root.elem)
		self.R_In_order_Traversal(root.lchild)
		self.R_In_order_Traversal(root.rchild)
	#Pre order 
	def R_Pre_order_Traversal(self,root):
		if root == None:
			return 
		self.R_Pre_order_Traversal(root.lchild)
		self.presult.append(root.elem)
		self.R_Pre_order_Traversal(root.rchild)
	#Post order
	def R_Pose_order_Traversal(self,root):
		if root == None:
			return
		self.R_Pose_order_Traversal(root.lchild)
		self.R_Pose_order_Traversal(root.rchild)
		self.poresult.append(root.elem)
	#------Traversal: Stack version-------#
	# In order
	def S_In_order_Traversal(self,root):
		if root == None:
			return
		mystack = []
		node = root
		result = []
		while node or mystack:
			while node:
				result.append(node.elem)
				mystack.append(node)
				node = node.lchild
			node = mystack.pop()
			node = node.rchild
		print(result)
	def S_Pre_order_Traversal(self,root):
		if root == None:
			return
		mystack = []
		node = root
		result = []
		while node or mystack:
			while node:
				mystack.append(node)
				node  = node.lchild
			node = mystack.pop()
			result.append(node.elem)
			node = node.rchild
		print(result)
	#Post order 
	# find the anti order by array and then pop out one by one
	def S_Post_order_Traversal(self,root):
		if root == None:
			return
		mystack1 = []
		mystack2 = []
		node = root
		mystack1.append(node)
		result = []
		while mystack1:
			node = mystack1.pop()
			if node.lchild:
				mystack1.append(node.lchild)
			if node.rchild:
				mystack1.append(node.rchild)
			mystack2.append(node)
		while mystack2:
			result.append(mystack2.pop().elem)
		print(result)


if __name__ == '__main__':
	elems = range(10)
	tree = Tree()
	for elem in elems:                  
		tree.add_item(elem)
	tree.R_Pre_order_Traversal(tree.root)
	print("====")
	tree.S_Pre_order_Traversal(tree.root)
	tree.S_Post_order_Traversal(tree.root)





