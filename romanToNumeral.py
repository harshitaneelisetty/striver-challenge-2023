    #https://www.codingninjas.com/codestudio/problems/roman-numeral-to-integer_8230780?challengeSlug=striver-sde-challenge

    def romanToInt(s):
        lst = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev = 1000
        for i in s:
            if lst[i] > prev:
                result -= prev * 2
            prev = lst[i]
            result += lst[i]
        return result
      
      #firstly i initialized a variable result to 0, which will store the final integer value
      #and also initialised a variable prev to 1000, representing the value of the previous Roman numeral character encountered
      #i iterated over each character i in the input string s
      #for each chraacter i compared its corresponding integer value from the lst dictionary with the previous value prev
      #if the current value is greater than the previous value, it means that a subtraction rule is being applied
      #in that case i subtracted twice from the result to undo the addition made in the previous iteration
      #then i updated res based on the subtraction rule and i updated 
      #the prev variable to the current character's value from the lst dictionary and added it to the result
      
      
      
      
      
      
      
