#https://www.codingninjas.com/codestudio/problems/implement-atoi-function_8230776?challengeSlug=striver-sde-challenge

def atoi(string):
    is_negative = 0
    if string[0] == '-':
        is_negative = 1
    number = 0
    for i in range(len(string)):
        if string[i] >= '0' and string[i] <= '9':
            digit = ord(string[i]) - ord('0')
            number = number * 10 + digit
    if is_negative:
        number *= -1
    return number

  #i initialised a variable is_negative to 0, which will be used to track if the integer should be negative
  #i checked if the first character of the input string is a hyphen
  #if it is i setted is_negative to 1 indicating that the resulting integer should be negative
  #i initialised a variable numbert to 0 which will store the final integer value
  #i iterated over each character string[i] in the input string
  #for each charcter i checked if it is a digit from '0' to '9' by comparing its ASCII value
  #If the character is a digit i calculated the corresponding integer value by subtracting the ASCII value of '0' from the ASCII value of the character
  #then i multiplied the current value of number by 10 and added the calculated digit to it
  
  
  
  
  
  
  
  
