#https://www.codingninjas.com/codestudio/problems/maximum-product-subarray_8230828?challengeSlug=striver-sde-challenge

   def maximumProduct(nums, n):
        product1 = nums[0]
        product2 = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            temp = max(nums[i], product1 * nums[i], product2 * nums[i])
            product2 = min(nums[i], product1 * nums[i], product2 * nums[i])
            product1 = temp
            res = max(res, product1)
        return res
      
#i initialised 3 variables product1, product2, and res to store maximum product found so far, the second maximum product found so far, and the overall maximum product.
#i started iterating over nums leaving index 0
#inside loop i calculated the maximum product of the current element nums[i]
#i took max of product1 * nums[i] or product2 * nums[i] or simply nums[i]
#updated the value of product2 to be the minimum product of the current element nums[i] with either product1 * nums[i] or product2 * nums[i] or simply nums[i]
#updated the value of product1 to be the maximum product
#updated res to be the maximum value among the current res and the updated product1
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      

