'''
!/usr/bin/python
 -*- coding: utf-8 -*-
 This is string class solution for Leetcode questions
 @ author Yongjun Chen
LeetCode
'''
#leetcode solutions
class String(object):
	def __init__(self):
		pass
	#--------String-------#
	def romanToInt(self, s):
		roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
		z = 0
		for i in range(0, len(s) - 1):
		    if roman[s[i]] < roman[s[i+1]]:
		        z -= roman[s[i]]
		    else:
		        z += roman[s[i]]
		return z + roman[s[-1]]
	def isValid(self, s):
		stack = []
		left_part = set(['(','[','{'])
		right_part = set([')',']','}'])
		for item in s:
			if item in left_part:
				stack.append(item)
			elif item in right_part:
				if len(stack)>0:
					top = stack.pop()
				else:
					return False
			if item == ')' and top != '(' or item == ']' and top != '[' or item =='}' and top != '{':
				return False
		if len(stack) == 0:
			return True
		else:
			return False
	#58. Length of Last Word
	def lengthOfLastWord(self, s):
		length = 0
		for index in range(len(s)):
			if index < len(s)-1 and s[index] == ' ':
				length = 0
			elif index == len(s)-1 and s[index] == ' ':
				length = length
			else:
				length += 1
		return length
	# 344. Reverse String
	def reverseString(self, s):
		return s[::-1]
	#434. Number of Segments in a String
	def countSegments(self, s):
		Isword = False
		result = 0
		for index in range(len(s)):
			if s[index] is not ' ':
				Isword = True
			if s[index] is ' ' and Isword is True:
				result += 1
			elif index == len(s)-1 and Isword is True:
				result += 1
		return result

	#--------Median--------#
	def lengthOfLongestSubstring(self, s):
		maxsub = 0
		currentsub = 0
		temset = set()
		for index in range(len(s)):
			if s[index] not in temset:
				temset.add(s[index])
			else:
				currentsub = len(temset)
				maxsub = max(maxsub,currentsub)
				temset = set(s[index])
		currentsub = len(temset)
		maxsub = max(maxsub,currentsub)
		return maxsub 

if __name__ == '__main__':
	s = String()
	test = "([)]"
	print(s.isValid(test))
	print(s.lengthOfLastWord('a '))
	s = 'abcd'
	print(s[::2])







