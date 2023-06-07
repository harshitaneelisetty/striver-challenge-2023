#https://www.codingninjas.com/codestudio/problems/pair-sum_8230699?challengeSlug=striver-sde-challenge

def pairSum(arr, s):
    n = len(arr)
    ans = []
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == s:
                pair = [arr[i], arr[j]]
                ans.append(pair)
    res = [[min(a, b), max(a, b)] for a, b in ans]
    res = sorted(res, key=lambda x: x[0])
    return res
  
#I iterated over each element in the array
#checked all possible pairs using nested loops
#If a pair with the desired sum is found, it is added to the ans list.
#The res list is then created to store the pairs in a sorted manner
#and it is sorted based on the first element of each pair
