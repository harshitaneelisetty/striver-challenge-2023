#https://www.codingninjas.com/codestudio/problems/combination-sum-ii_8230820?challengeSlug=striver-sde-challenge

  def combinationSum2(candidates, n, target):
        def backtrack(nums, targetLeft, path):
            if targetLeft == 0:
                res.append(path)
                return
            
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                if nums[i] > targetLeft:
                    break
                backtrack(nums[i + 1 : ],targetLeft - nums[i], path + [nums[i]])    
            
        res = []
        backtrack(sorted(candidates), target, [])
        return res
      
      #I found all combination of numbers from the candidates list that sum up to given target by uisng backtracking
      #i avoided duplicates combinations by skipping the same number at the same level of recursion. 
