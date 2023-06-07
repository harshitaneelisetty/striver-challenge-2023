#https://www.codingninjas.com/codestudio/problems/majority-element-ii_8230738?challengeSlug=striver-sde-challenge


def majorityElementII(nums):
	n = len(nums)
	ans = []
	count = Counter(nums)
	for k, v in count.items():
		if v > n // 3:
			ans.append(k)
	return ans
  
  #I used counter method to find freq of each element and compared with n // 3
  
