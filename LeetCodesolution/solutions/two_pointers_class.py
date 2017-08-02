'''
!/usr/bin/python
 -*- coding: utf-8 -*-
 This is two pointers class solution for Leetcode questions
 @ author Yongjun Chen
LeetCode
'''

#leetcode solutions
class two_pointers(object):
	def __init__(self):
		pass

	def threeSum(self, nums):
		nums.sort()
		res = []
		for i in range(len(nums)-2):
		 	if i >0 and nums[i] == nums[i-1]:
		 		continue
		 	j, k = i + 1,len(nums)-1
		 	while j < k:
		 		if (nums[i] + nums[j] + nums[k] == 0):
		 			res.append([nums[i],nums[j],nums[k]])
		 			j += 1
		 			k -= 1
		 			while (j < k and nums[j] == nums[j-1]):
		 				j += 1
		 			while (j < k and nums[k] == nums[k+1]):
		 				k -= 1
		 		elif (nums[i] + nums[j] + nums[k] < 0):
		 			j += 1
		 		else:
		 			k -= 1
		return res

	def threeSumClosest(self, nums, target):
		nums.sort()
		result = nums[0] + nums[1] + nums[2]
		for i in range(len(nums)-2):
			j, k = i+1, len(nums) - 1
			while j < k:
				threesum = nums[i] + nums[j] + nums[k]
				if threesum == target:
					return threesum
				if abs(target-threesum) < abs(target-result):
					result = threesum
				if threesum < target:
					j += 1
				elif threesum > target:
					k -= 1
		return result

	def threeSunClosest_my(self,nums,target):
		nums.sort()
		i = 0
		j = 1
		k = 2
		res = nums[i] + nums[j] + nums[k]
		while i < len(nums)-2:
			if k < len(nums)-1:
				k += 1
				print(k)
			elif j < len(nums)-2:
				j += 1
			elif i < len(nums)-3:
				i += 1
			if abs(target -(nums[i] + nums[j] + nums[k])) == abs(target-res):
				continue
			elif abs(target -(nums[i] + nums[j] + nums[k])) < abs(target-res):
				res = nums[i] + nums[j] + nums[k]
				if i == len(nums)-3:
					return res
			else:
				return res

	def fourSum(self, nums, target):
		def forNsum(nums, target, N, result, results):
			if len(nums)< N or N < 2 or target < nums[0]*N or target > nums[-1]*N:
				return 
			if N == 2:
				l, r = 0, len(nums)-1
				while l < r:
					sums = nums[l] + nums[r]
					if sums == target:
						results.append(result+[nums[l],nums[r]])
						l+=1
						while l < r and nums[l] == nums[l-1]:
							l+=1
					elif sums < target:
						l += 1
					else:
						r -= 1
			else:
				for i in range(len(nums)-N+1):
					if i == 0 or (i > 0 and nums[i-1] != nums[i]):
						forNsum(nums[i+1:], target-nums[i],N-1,result+[nums[i]],results)
		nums.sort()
		results = []
		forNsum(nums, target,4,[],results)
		return results

	def sortColors(self, nums):
		i = 0 
		j = len(nums)-1
		k = 0
		while i <= k and k <= j:
			if nums[k] == 0:
				temp = nums[i]
				nums[i] = nums[k]
				nums[k] = temp
				i += 1
				k += 1
			elif nums[k] == 1:
				k += 1
			else:
				temp = nums[j]
				nums[j] = nums[k]
				nums[k] = temp
				j -= 1
		return nums

	def removeDuplicates_part(self, nums):
		dic = {}
		for index, item in enumerate(nums):
			dic[item] = min(dic.get(item,0),1) + 1
		return sum(dic.values())

	def removeDuplicates(self, nums):
		#  go through the numbers and include those in the result that haven't been included twice already
		i = 0
		for number in nums:
			if i<2 or number > nums[i-2]:
				nums[i] = number
				i += 1
		return i
if __name__ == '__main__':
	t = two_pointers()
	nums = [1,1,1,2]
	print(t.sortColors(nums))	
	print(t.removeDuplicates(nums))																