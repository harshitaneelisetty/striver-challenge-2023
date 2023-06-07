#https://www.codingninjas.com/codestudio/problems/day-6-majority-element_8230731?challengeSlug=striver-sde-challenge

from collections import Counter

def findMajorityElement(nums, n):
	count = Counter(nums)
	for k, v in count.items():
		if v > n // 2:
			return k
	return -1
	
  #I used the counter method to find frequency of each element
  #then I iterated over the dict and compare the val with n // 2 
