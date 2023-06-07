#https://www.codingninjas.com/codestudio/problems/count-subarrays-with-given-xor_8230830?challengeSlug=striver-sde-challenge
def subarraysXor(arr, k):
    n = len(arr)
    xr = 0
    mpp = {}
    mpp[xr] = 1
    cnt = 0

    for i in range(n):
        xr = xr ^ arr[i]
        x = xr ^ k
        cnt += mpp.get(x, 0)
        mpp[xr] = mpp.get(xr, 0) + 1

    return cnt
  
#I used a sliding window approach and a frequency map.
#I initialsed the xor value to 0 and created a freq map with initial count 1 
#then iterates through each element in arr and updates xr by XORing it with the current element.
#next, i calculated the target XOR value x by XORing xr with k. If x exists in the frequency map, it means there are subarrays whose XOR is equal to k
#incremented count
