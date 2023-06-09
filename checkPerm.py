#https://www.codingninjas.com/codestudio/problems/check-permutation_8230834?challengeSlug=striver-sde-challenge

def areAnagram(str1, str2):
    return 1 if sorted(str1) == sorted(str2) else 0
  
 #i sorted the two string if they contains same charcters then its sort should be same
 #i compared two sorted strings whether they are equal or not
