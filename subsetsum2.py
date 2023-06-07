  #https://www.codingninjas.com/codestudio/problems/subsets-ii_8230855?challengeSlug=striver-sde-challenge

  def uniqueSubsets(n :int, nums :List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        def helper(idx, nums, ds):
            x = [i for i in ds]
            ans.append(x)
            for i in range(idx, len(nums)):
                if i != idx and nums[i] == nums[i - 1]:
                    continue
                ds.append(nums[i])
                helper(i + 1, nums, ds)
                ds.pop()
        helper(0, nums, [])
        return ans
     
    #I explored all possibilites, I used a helper function that takes an index idx, the original array nums, and a current subset ds
    #i appended each  unique subset encountered to the ans list while avoiding duplicates by skipping identical elements at different indices
