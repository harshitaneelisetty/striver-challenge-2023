#https://www.codingninjas.com/codestudio/problems/chess-tournament_8230779?challengeSlug=striver-sde-challenge

def chessTournament(positions, n, c):
    positions.sort()
    ans = 0
    l = 1
    r = positions[n-1]
    while l <= r:
        mid = (l + r) // 2
        count = 1
        previous_room = positions[0]
        for i in range(1, n):
            if positions[i] - previous_room >= mid:
                count += 1
                previous_room = positions[i]
        
        if count >= c:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    
    return ans

  #i used binary search algorithm  to find the largest minimum distance between chess tournament positions
  #such that at least c players can be assigned to each position
  #i iteratively adjusted the search range based on the number of players that can be accommodated until the maximum minimum distance
  
  
  
  
  
  
  
