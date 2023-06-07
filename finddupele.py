#https://www.codingninjas.com/codestudio/problems/find-duplicate-in-array_8230816?challengeSlug=striver-sde-challenge

def findDuplicate(nums):
    slow = nums[0]
    fast = nums[0]
    while True:
        fast = nums[nums[fast]]
        slow = nums[slow]
        if fast == slow:
            break
    fast = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow

  #I used   Floyd's Tortoise and Hare algorithm, also known as the "Cycle Detection" algorithm.
  # I used two pinters slow and fasr to detect a cycle.
  # Now i am trying to find the meeting points of the two pointers within cycle
  #then resets the fast pointer and moves both pointers at the same speed until they meet again, which identifies the duplicate number.
