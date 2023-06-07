#https://www.codingninjas.com/codestudio/problems/remove-duplicates-from-sorted-array_8230811?challengeSlug=striver-sde-challenge

  def removeDuplicates(nums,n):
        #n = len(nums)
        if n == 0:
            return 0
        i = 0
        for j in range(1, n):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1
      
    #we know that array is sorted so the duplicates elements come together
    #so i checked addjacent elements, if adjacent elements are different i added to the list
