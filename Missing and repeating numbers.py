#https://www.codingninjas.com/codestudio/problems/missing-and-repeating-numbers_8230733?challengeSlug=striver-sde-challenge

def missingAndRepeating(arr, n):
    count = Counter(arr)
    ans = []
    for i in range(1, n + 1):
        if count[i] == 0:
            ans.append(i)
    for k,v in count.items():
        if v == 2:
            ans.append(k)  
    return ans  
 #I used counter to get val and freq of value
 # then i checked for count 0 ie missing element
 # again iterated to find repeating number
 
