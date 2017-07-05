#leetcode solutions

class Solution(object):
	#---------initial-------#
	def __init__(self):
		pass
	#---------Array---------#
	#1 twoSum
	def twoSum(self,nums,target):
		if len(nums)<=1:
			return False
		buf_dict = {}
		for i in range(len(nums)):
			if nums[i] in buf_dict:
				return [buf_dict[nums[i]],i]
			else:
				buf_dict[target-nums[i]] = i
	#26 Remove Duplicates from Sorted Array
	def removeDuplicates(self,nums):
		index = 0
		while True:
			if index >= (len(nums)-1):
				break
			if nums[index] == nums[index+1]:
				nums.pop(index)
				index = index - 1
			index += 1
		return len(nums),nums
	#27 removeElement 
	def removeElement(self, nums, val):
		index = 0
		length = len(nums)
		for i in range(length):
			if nums[index] == val:
				nums.pop(index)
				index -= 1
			index += 1
		return len(nums),nums
	#35 searchInsert
	def searchInsert(self, nums, target):
		result = 0
		for index in range(len(nums)):
			if nums[index] == target:
				result = index
			if nums[index] < target:
				result = index +1
		return result
	#53 maxSubArray
	def maxSubArray(self,nums):
		currentsum = nums[0]
		maxsum     = nums[0]
		for item in nums[1:]:
			currentsum = max(item, currentsum+item)
			maxsum     = max(currentsum, maxsum)
		return maxsum
	#88. Merge Sorted Array
	def merge(self, nums1, m, nums2, n):
		result = [0] * (len(nums1) + len(nums2))
		i = 0
		j = 0
		while i+j <= m + n -1:
			if j >= n or (i < m and nums1[i] < nums2[j]) :
				result[i+j] = nums1[i]
				i += 1
			elif i >=m or (j < n and nums1[i] >=  nums2[j]) :
				result[i+j] = nums2[j]
				j += 1
		return result
	#118. Pascal's Triangle
	def sumlist_element(self,list1,list2):
		result = [(x+y) for x, y in zip(list1, list2)]
		return result

	def generate(self, numRows):
		result = []
		current = [1]
		for index in range(numRows):
			result.append(current)
			right = current + [0]
			left = [0] + current
			current = self.sumlist_element(left,right)
		return result

	def getRow(self,rowIndex):
		result = []
		current = [1]
		for index in range(rowIndex):
			result.append(current)
			right = current + [0]
			left = [0] + current
			current = self.sumlist_element(left,right)
		return result[rowIndex-1]
	#121. Best Time to Buy and Sell Stock
	def maxProfit(self, prices):
		profix = 0
		if len(prices) == 0:
			return profix
		else:
			minprice = prices[0]
			for price in prices:
				if price < minprice:
					minprice = price 
				elif price-minprice > profix:
					profix = price -minprice
			return profix
	#122. Best Time to Buy and Sell Stock II
	def maxProfit2(self, prices):
		profix = 0
		if len(prices) < 2:
			return profix
		else:
			minvalue = []
			maxvalue = []
			for index in range(len(prices)):
				if (index == 0 and prices[index] < prices[index+1]):
					minvalue.append(prices[index])
				elif index == len(prices)-1 and prices[index-1] < prices[index]: 
					maxvalue.append(prices[index])
				elif 0 < index < len(prices)-1 and prices[index-1] >= prices[index] and prices[index] < prices[index+1]:
					minvalue.append(prices[index])
				elif 0 < index < len(prices)-1 and prices[index-1] < prices[index] and prices[index] >= prices[index+1]:
					maxvalue.append(prices[index])
				if minvalue and maxvalue:
					profix += (maxvalue.pop()-minvalue.pop())
			return profix
	#167. Two Sum II - Input array is sorted
	def twoSum2(self, numbers, target):
		i = 0
		j = len(numbers)-1
		while i < j:
			if numbers[i] + numbers[j] > target:
				j-=1
			elif numbers[i] + numbers[j]< target:
				i+=1
			else: 
				return i+1, j+1
	#169. Majority Element
	def majorityElement(self, nums):
		dic = {}
		for element in nums:
			dic[element] = dic.get(element,0) + 1
		for index in dic.keys():
			if dic[index] > len(nums)/2:
				return index
	#189. Rotate Array
	def rotate(self, nums, k, Type):
		n = len(nums)
		result = [0] * n
		if Type == 'Frist':
			for i in range(n):
				if i < k:
					result[i] = nums[n-k+i]
				else:
					result[i] = nums[i-k]
			for i in range(n):
				nums[i] = result[i]
			return nums
		elif Type == 'Second':
			nums[:] = nums[(n-k):] + nums[:(n-k)]
			return nums
	#217. Contains Duplicate
	def containsDuplicate(self, nums):
		if len(nums) <= 1:
			return False
		dic = {}
		index = 0
		while True:
			dic[nums[index]] = dic.get(nums[index],0) + 1
			if dic[nums[index]] > 1:
				return True
			else:
				index += 1
			if index == len(nums):
				return False
	#268. Missing Number
	def missingNumber(self, nums):
		s = set([i for i in range(len(nums)+1)])
		for i in nums:
			if i in s:
				s.remove(i)
		return list(s)[0]
	#283. Move Zeroes
	def moveZeroes(self, nums):
		zero = 0 
		for i in range(len(nums)):
			if nums[i] != 0:
				nums[i], nums[zero] = nums[zero], nums[i]
				zero += 1
		return nums
	#414. Third Maximum Number
	def thirdMax(self, nums):
		maxlist = [float('-inf'),float('-inf'),float('-inf')]
		for item in nums:
			if item > maxlist[-1]:
				maxlist.append(item)
				maxlist.pop(0)
			elif item > maxlist[-2] and item < maxlist[-1]:
				maxlist.insert(-1,item)
				maxlist.pop(0)
			elif item > maxlist[-3] and item < maxlist[-2]:
				maxlist.insert(-2,item)
				maxlist.pop(0)
		if maxlist[0] == float('-inf'):
			return maxlist[-1]
		else:
			return maxlist[0]
	#485. Max Consecutive Ones
	def findMaxConsecutiveOnes(self, nums):
		currentones = 0
		maxones = 0
		for item in nums:
			if item == 1:
				currentones += 1
			else:
				currentones = 0
			if maxones < currentones:
				maxones = currentones
		return maxones
	#532. K-diff Pairs in an Array
	def findPairs(self, nums, k):
		if k > 0:
			return len(set(nums) & {n+k for n in nums})
		elif k  == 0:
			dic = {}
			result = 0
			for item in nums:
				dic[item] = dic.get(item,0) + 1
			for nums in dic.values():
				if nums > 1:
					result += 1
			return result
		else:
			return 0
	#561. Array Partition I
	def arrayPairSum(self, nums):
		result = 0
		nums.sort()
		for index in range(0,len(nums)-1,2):
			result += nums[index]
		return result
if __name__ == '__main__':
	s= Solution()
	nums = [1,2,-2,1]
	list1 = [1,3,1,5,4]
	#print(s.findPairs(list1,0))
	list2 = [1,4,3,2]
	print(s.arrayPairSum(list2))
	#print(s.findMaxConsecutiveOnes(list1))



