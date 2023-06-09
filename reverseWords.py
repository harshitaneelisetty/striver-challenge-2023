#https://www.codingninjas.com/codestudio/problems/reverse-words-in-a-string_8230698?challengeSlug=striver-sde-challenge

def reverseString(str: str) -> str:
    str = str.lstrip()
    str = str.rstrip()
    lst = str.split(" ")
    s = ''
    for i in lst[::-1]:
        i = i.lstrip()
        i = i.rstrip()
        s += i + " " 
    return s

 #firstly i used lstrip and rstrip functions to remove the white spaces left and right
 #then i splittedthe word and i iterated by reversing the word
 #for each word in str i removed the white spaces left and right and i added to the ans
