'''
!/usr/bin/python
 -*- coding: utf-8 -*-
 This is dynamic programming class solution for Leetcode questions
 @ author Yongjun Chen
LeetCode
'''
import math
#leetcode solutions
class dynamic_programming(object):
	def __init__(self):
		pass
	#------ Easy ------#
	#53 maxSubArray
	def maxSubArray(self,nums):
		currentsum = nums[0]
		maxsum     = nums[0]
		for item in nums[1:]:
			currentsum = max(item, currentsum+item)
			maxsum     = max(currentsum, maxsum)
		return maxsum
	#198. House Robber
	''' 
	dp func:
	f0 = nums[0]
	f1 = max(nums[0],nums[1])
	f2 = max(f0 + nums[2], f1)
	...
	fn = max(fn-2 + nums[n], fn-1)
	last = now
	now = max(last + i, now)
	'''
	def rob(self, nums):
		last = 0
		now  = 0
		for item in nums:
			last,now  = now, max(last+item,now)
		return now

	#--------Median---------#
	def uniquePaths(self, m, n):
		if m == 1 or n == 1:
		    return 1
		return int(math.factorial(m+n-2)/(math.factorial(m-1)*(math.factorial(n-1))))

	def uniquePathsWithObstacles(self, obstacleGrid):
		m = len(obstacleGrid); n = len(obstacleGrid[0])
		obsnums = 0
		for index in range(m):
			obsnums += sum(obstacleGrid[index])
		if m == 1 or n == 1:
		    if obsnums == 0:
		    	return 1
		    else:
		    	return 0
		print(math.factorial(m+n-2))
		print((math.factorial(m-1)*(math.factorial(n-1)))-obsnums*4)
		return max(int(math.factorial(m+n-2)/(math.factorial(m-1)*(math.factorial(n-1)))-obsnums*4),0)

	def minPathSum(self, grid):
		w = len(grid)
		h = len(grid[0])
		for index in range(1,w):
			grid[index][0] += grid[index-1][0]
		for index in range(1,h):
			grid[0][index] += grid[0][index-1]
		for i in range(1,w):
			for j in range(1,h):
				grid[i][j] += min(grid[i-1][j],grid[i][j-1])
		return grid[-1][-1]
	# G(n): the number of unique BST for a sequence of length n.
	# F(i, n): F(i, n) = G(i-1) * G(n-i).the number of unique BST, when i is the root.
	# So: G(n) = G(0) * G(n-1) + G(1) * G(n-2) + … + G(n-1) * G(0) 
	# So we need G(n-1) before G(n)
	def numTrees(self, n):
		G = [0]*(n+1)
		G[0] = 1
		G[1] = 1
		for outer in range(2,n+1):
			for inner in range(1,outer+1):
				G[outer] += G[outer-inner]*G[inner-1]
		return G[-1]
		

if __name__ == '__main__':
	s = dynamic_programming()
	grid = [[1,2,3],[3,1,2]]
	print(s.minPathSum(grid))
	print(s.numTrees(3))

