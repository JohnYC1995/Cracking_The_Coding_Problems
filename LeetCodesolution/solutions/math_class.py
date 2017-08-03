'''
!/usr/bin/python
 -*- coding: utf-8 -*-
 This is math class solution for Leetcode questions
 @ author Yongjun Chen
LeetCode
'''

#leetcode solutions
class math(object):
	def __init__(self):
		pass

	def mySqrt(self, x, n):
	    r = x
	    while r*r > x:
	        r = (r + x/r) / 2
	    return r

	def isPowerOfTwo(self,n):
		if n == 1 or n ==2:
			return True
		if n > 2:
			return self.isPowerOfTwo(n/2.0)
		if n < 2:
			return False

	def isUgly(self, num):
		for prime in 2,3,5:
			while num % prime == 0 and num>0:
				num /= prime
		return num == 1

	def isPerfectSquare(self, num):
		if num < 1:
			return False
		elif num == 1:
			return True
		r = num/2
		while r*r > num:
			r = (r+num//r) // 2
		if r*r == num:
			return True
		else:
			return False

	def maxRotateFunction(self, A):
		#F(k) = F(k-1) + sum - nBk[0]
		allsum = sum(A)
		F = 0
		for i in range(len(A)):
			F += i*A[i]
		maxvalue = F
		for i in range(len(A)-1,0,-1):
			F = F + allsum -len(A)*A[i]
			maxvalue = max(F, maxvalue)
		return maxvalue

	def integerReplacement(self, n):
		if n == 1:
			return 0
		if n % 2 == 0:
			return 1 + self.integerReplacement(n/2)
		else:
			return min(self.integerReplacement((n-1)/2)+2, self.integerReplacement((n-1)/2+1)+2)

	def minMoves2(self, nums):
		median = sorted(nums)[len(nums) // 2]
		print(median)
		return sum(abs(num - median) for num in nums)

if __name__ == '__main__':
	test = 25
	s= math()
	#print(s.isPowerOfTwo(test))
	#print(s.isPerfectSquare(test))
	A = [4, 3, 2, 6]
	#print(s.maxRotateFunction(A))
	#print(s.integerReplacement(7))
	print(s.minMoves2([1,1,3,3]))
