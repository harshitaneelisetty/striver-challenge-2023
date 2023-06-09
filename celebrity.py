#https://www.codingninjas.com/codestudio/problems/the-celebrity-problem_8230781?challengeSlug=striver-sde-challenge

def findCelebrity(n, knows):
    ids = []
    for i in range(n):
        ids.append(i)

    while len(ids) > 1:
        id1 = ids.pop()
        id2 = ids.pop()
        if knows(id1, id2):
            ids.append(id2)
        else:
            ids.append(id1)

    celebrity = ids[len(ids) - 1]

    know_any = False
    known_to_all = True

    for i in range(n):
        if knows(celebrity, i):
            know_any = True
            break

    for i in range(n):
        if i != celebrity and not knows(i, celebrity):
            known_to_all = False
            break

    if know_any or not known_to_all:
        celebrity = -1

    return celebrity

#firsty i started by creating a list of all the person IDs from 0 to n-1
#then in a looop i repeatedly took takes two IDs from the list, checked if the first person knows the second person using the knows function
#and i kept only the person who is known
#i processed until there is only one person left in the list, which is considered a celebrity
#next i checked if all other people know the celebrity
#i iterated over all the people again and checked if each person expect the celebrity itself
#if there is at least one person who doesn't know the celebrity, i setted the variable known_to_all to False.
#finally, based on the values of know_any and known_to_all, i determined whether the celebrity is a valid celebrity
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  


