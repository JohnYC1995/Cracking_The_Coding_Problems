'''
!/usr/bin/python
 -*- coding: utf-8 -*-
 This is breadth first search class solution for Leetcode questions
 @ author Yongjun Chen
LeetCode
'''
from TreeNode import *
#leetcode solutions
class Breadth_first_Search(object):
	def __init__(self):
		pass

	def minDepth(self, root):
		if not root:
			return 0
		elif not root.left:
			return 1 + self.minDepth(root.right)
		elif not root.right:
			return 1 + self.minDepth(root.left)
		else:
			return 1 + min(self.minDepth(root.left),self.minDepth(root.right))
	
	def levelOrderBottom(self, root):
		res, data = [], []
		if not root:
			return res
		queue = []
		queue.append(root)
		Nodenums = 1
		while queue:
			node = queue.pop(0)
			data += [node.val]
			Nodenums -= 1
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)
			if Nodenums == 0:
				res = [data] + res
				Nodenums = len(queue)
				data = []
		return res

	def levelOrder(self, root):
		res, data = [], []
		if not root:
			return res
		queue = []
		queue.append(root)
		Nodenums = 1
		while queue:
			node = queue.pop(0)
			data += [node.val]
			Nodenums -= 1
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)
			if Nodenums == 0:
				res += [data]
				data = []
				Nodenums = len(queue)
		return res

	def zigzagLevelOrder(self, root):
		res, data = [], []
		if not root:
			return res
		queue = []
		queue.append(root)
		Nodenums = 1
		levelnums = 1
		while queue:
			node = queue.pop(0)
			if levelnums % 2 == 1:
				data += [node.val]
			else:
				data = [node.val] + data
			Nodenums -= 1
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)		
			if Nodenums == 0:
				res += [data]
				data = []
				Nodenums = len(queue)
				levelnums += 1
		return res

	def solve(self, board):
		if not board:
			return 
		width, height = len(board),len(board[0])
		boardqueue = [index for k in range(max(width,height)) \
							for index in ((0,k),(width-1,k),(k,0),(k,height-1))]
		print("boardqueue",boardqueue)
		while boardqueue:
			x, y = boardqueue.pop(0)
			if 0 <= x < width and 0 <= y < height and board[x][y] == 'O':
				board[x][y] = '1'

				boardqueue += [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
		print("changed board",board)
		for i in range(width):
			for j in range(height):
				if board[i][j] == '1':
					board[i][j] = 'O'
				elif board[i][j] == 'O':
					board[i][j] = 'X'
		return board





if __name__ == '__main__':
	width = 3
	height =4
	boardqueue = [index for k in range(max(width,height)) \
							for index in ((0,k),(width-1,k),(k,0),(k,height-1))]

	print(boardqueue)



