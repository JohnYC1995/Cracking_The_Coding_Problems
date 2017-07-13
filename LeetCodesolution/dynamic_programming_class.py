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

if __name__ == '__main__':
	s = dynamic_programming()
	grid = [[0,0],[1,0]]
	print(s.uniquePathsWithObstacles(grid))




