#https://www.codingninjas.com/codestudio/problems/minimum-number-of-platforms_8230720?challengeSlug=striver-sde-challenge

def calculateMinPatforms(arr, dep, n):
    arr2 = []
    for i in range(n):
        arr2.append([arr[i], dep[i]])
    arr2.sort()  
    p = []
    count = 1
    heapq.heappush(p, arr2[0][1])
    for i in range(1, n):
        if p[0] >= arr2[i][0]:
            count += 1
        else:
            heapq.heappop(p)
        heapq.heappush(p, arr2[i][1])
    return count

   # i sorted the times based on the arrival times, and uses a min-heap to keep track of the platforms needed
    #i iterated through the sorted list and increments the count of platforms
    #if the minimum departure time in the heap is greater than or equal to the arrival time of the current train
    #otherwise i removed the minimum departure time from the heap and added the departure time of the current train
