  #https://www.codingninjas.com/codestudio/problems/count-and-say_8230807?challengeSlug=striver-sde-challenge

  def writeAsYouSpeak(n):
        output = '1'
        for i in range(n-1):
            output = ''.join([str(len(list(g))) + k for k, g in groupby(output)])
        return output
   
  #i iterated n - 1 times. in each iteration i applied a transformation to the op strung
  #i done transformations using groupby func
  #by groupby function i grouped consecutive characters in the output string
 
   
