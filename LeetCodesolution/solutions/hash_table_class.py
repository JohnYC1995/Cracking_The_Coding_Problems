'''
!/usr/bin/python
 -*- coding: utf-8 -*-
 This is hash table class solution for Leetcode questions
 @ author Yongjun Chen
LeetCode
'''
from collections import Counter

#leetcode solutions
class hash_table(object):
	def __init__(self):
		pass

	def singleNumber(self, nums):
		result = nums[0]
		for i in range(1,len(nums)):
			result = result^nums[i]
		return result

	def findRepeatedDnaSequences(self, s):
		if len(s)<10:
			return []
		dic = {}
		result = []
		for i in range(10,len(s)+1):
			dic[s[i-10:i]] = dic.get(s[i-10:i],0) + 1
		for key,item in dic.items():
			if item > 1:
				result.append(key)
		return result

	def isAnagram(self, s,t):
		dic1, dic2 = {}, {}
		for item in s:
		    dic1[item] = dic1.get(item, 0) + 1
		for item in t:
		    dic2[item] = dic2.get(item, 0) + 1
		return dic1 == dic2

	def getHint(self, secret, guess):
		import collections
		dict_s, dict_g = collections.Counter(secret),collections.Counter(guess)
		nums_a = sum(i==j for i, j in zip(secret,guess))
		print(dict_s & dict_g)
		return '%sA%sB' % (nums_a, sum((dict_s & dict_g).values())-nums_a)

	def fourSumCount(self, A, B, C, D):
		import collections
		AaddB = collections.Counter(a+b for a in A for b in B)
		return sum(AaddB[-c-d] for c in C for d in D)
		
if __name__ == '__main__':
	## collections:
	#namedtuple()
	from collections import namedtuple
	from collections import defaultdict
	websites = [
	    ('Sohu', 'http://www.google.com/', u'张朝阳'),
	    ('Sina', 'http://www.sina.com.cn/', u'王志东'),
	    ('163', 'http://www.163.com/', u'丁磊')
	]
	Website = namedtuple('Website', ['name', 'url', 'founder'])
	for website in websites:
	    website = Website._make(website)
	    print (website)
	# Counter
	# see code above
	#defaultdict
	def my_factory():
		return 15
	result = defaultdict(my_factory)
	print(result['2'])










