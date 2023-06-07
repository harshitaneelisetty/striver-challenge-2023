#https://www.codingninjas.com/codestudio/problems/find-minimum-number-of-coins_8230766?challengeSlug=striver-sde-challenge

def findMinimumCoins(amount):
	count = 0
	for i in denominations[::-1]:
		while i <= amount:
			count += 1
			amount -= i
	return count

#inorder to get min coins i iterated through the denomintaions in reverse order
#i repeatedly subtracted the largest denomination from the amount until the amount becomes zero or less
#incremented the count each time then addded count to final ans



