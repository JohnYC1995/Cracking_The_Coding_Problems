'''
!/usr/bin/python
 -*- coding: utf-8 -*-
 This is backracking class solution for Leetcode questions
 @ author Yongjun Chen
LeetCode
'''
#leetcode solutions
class backtracking_search(object):
	def __init__(self):
		pass

	def readBinaryWatch(self, num):
		return ['%d:%02d' % (hour, minutes) for hour in range(12) for minutes in range(60) 
											if (bin(hour) + bin(minutes)).count('1') == num ]

if __name__ == '__main__':
	s = backtracking_search()
	print(s.readBinaryWatch(1))