'''
!/usr/bin/python
 -*- coding: utf-8 -*-
 This is depth first search class solution for Leetcode questions
 @ author Yongjun Chen
LeetCode
'''
from TreeNode import *
#leetcode solutions
class Depth_first_Search(object):
	def __init__(self):
		pass
	def test(self):
		test = 'a'
		return test

	def isSameTree(self, p, q):
		if p and q:
			return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
		else:
			return p == q

	def ismirror(self,root1,root2):
		if root1==None and root2==None:
			return True
		elif root1 and root2:
			return root1.val == root2.val and self.ismirror(root1.left,root2.right) and self.ismirror(root1.right,root2.left)
		else:
			return False

	def isSymmetric(self, root):
		return self.ismirror(root,root)

	def maxDepth(self, root):
		if root == None:
			return 0
		else:
			return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))

	def sortedArrayToBST(self, nums):
		if not nums:
			return None
		mid = len(nums)//2
		root = TreeNode(nums[mid])
		root.left = self.sortedArrayToBST(nums[:mid])
		root.right = self.sortedArrayToBST(nums[mid+1:])
		return root

if __name__ == '__main__':
	def test(a,b):
		if a and b :
			return a == b
		else:
			return False
	print(test(None,2))