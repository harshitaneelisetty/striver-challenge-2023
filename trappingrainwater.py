#https://www.codingninjas.com/codestudio/problems/trapping-rain-water_8230693?challengeSlug=striver-sde-challenge


def getTrappedWater(heights, n):
    peak = 0
    ans = 0
    if n == 0:
        return 0

    peakVal = heights[0]

    for i in range(n):
        if heights[i] >= peakVal:
            peak = i
            peakVal = heights[i]

    maxSoFar = float('-inf')
    countSubmerged = 0
    submergedArea = 0

    for i in range(peak + 1):
        if heights[i] >= maxSoFar:
            ans += countSubmerged * maxSoFar - submergedArea
            maxSoFar = heights[i]
            countSubmerged = 0
            submergedArea = 0
        else:
            submergedArea += heights[i]
            countSubmerged += 1

    maxSoFar = float('-inf')
    countSubmerged = 0
    submergedArea = 0

    for i in range(n - 1, peak - 1, -1):
        if heights[i] >= maxSoFar:
            ans += countSubmerged * maxSoFar - submergedArea
            maxSoFar = heights[i]
            countSubmerged = 0
            submergedArea = 0
        else:
            submergedArea += heights[i]
            countSubmerged += 1

    return ans
  
  #first i found the peak height in array
  #the i iterated from the left side of the peak
  #and calculated  the submerged area and count of submerged heights until it encounters a higher height
  #I added the trapped water for that section
  #then i iterated from the right side of the peak and does the same calculation.
  
  
  
  
