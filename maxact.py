#https://www.codingninjas.com/codestudio/problems/maximum-activities_8230800?challengeSlug=striver-sde-challenge

def maximumActivities(start, finish):
    n = len(start)
    activities = []
    for i in range(n):
        activities.append((finish[i], start[i]))

    activities.sort()
    maxActivity = 1
    currentTime = activities[0][0]

    for i in range(1, n):
        if activities[i][1] >= currentTime:
            maxActivity += 1
            currentTime = activities[i][0]

    return maxActivity
  
  #I sorted the activities based on their finish times, and then iterated through them
  #incremented count whenever an activitys start time is greater than or equal to the current time
  
  
  



