  #https://www.codingninjas.com/codestudio/problems/subset-sum_8230859?challengeSlug=striver-sde-challenge

  def subsetSum(arr: List[int]) -> List[int]:
        ans = []
        def helper(idx, ans, arr, N, sum):
            if idx == N:
                ans.append(sum)
                return
            helper(idx + 1, ans, arr, N, sum + arr[idx])
            helper(idx + 1, ans, arr, N, sum)
            
            
        arr.sort()
        helper(0, ans, arr, len(arr), 0)
        return sorted(ans)
      
    #I used helper recursive function to traverse the array and generate subsets by including or excluding each element
    #and then appened the calculated sum to ans list
    #final res is a sorted list
