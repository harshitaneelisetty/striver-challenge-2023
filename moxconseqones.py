#https://www.codingninjas.com/codestudio/problems/maximum-consecutive-ones_8230736?challengeSlug=striver-sde-challenge

def longestSubSeg(a, n, k):
    cnt0 = 0
    l = 0
    max_len = 0;
    for i in range(0, n):
        if a[i] == 0:
            cnt0 += 1
        while (cnt0 > k):
            if a[l] == 0:
                cnt0 -= 1
            l += 1
        max_len = max(max_len, i - l + 1);
    return max_len
  
 #I am trying to find the length of the longest subsegment with at most 'k' zeros by using a sliding window approach 
 #and keeping track of the count of zeros encountered.
