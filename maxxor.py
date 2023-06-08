#https://www.codingninjas.com/codestudio/problems/maximum-xor-of-two-numbers-in-an-array_8230852?challengeSlug=striver-sde-challenge

def maximumXor(nums):
    ans = 0
    mask = 0
    n = len(nums)
    num_set = set()

    for i in range(30, -1, -1):
        mask = mask | (1 << i)

        for j in range(n):
            num_set.add(nums[j] & mask)

        temp_ans = ans
        temp_ans = temp_ans | (1 << i)

        for num in num_set:
            if (num ^ temp_ans) in num_set:
                ans = temp_ans
                break

        num_set.clear()

    return ans

  #firstly i initialised ans to 0 to store max xor value. 
  #the variable mask is used to gradually set the bits from the msb to lsb
  #i iterated from 30 bits down to 0th bit.
  #for each bit position i setted the corresponding bit in the mask variable
  #then i iterated over the numbers in list and claculated AND with the mask and added the res to the num_set
  #net i created a ttemp_ans by setting the current bit in the answer
  #then i checked for each number num in the num_set if there exists another number in the set whose XOR with temp_ans is also present in the set
  # If such a pair is found, i updated the ans with temp_ans and breked the looop
  #after each bit position is processed the num_set is cleared and processed again
  
  
  
  
  
  
  
  
  
