#https://www.codingninjas.com/codestudio/problems/merge-intervals_8230700?challengeSlug=striver-sde-challenge

def mergeIntervals(intervals):
    n = len(intervals)
    intervals.sort()
    mergedIntervals = []

    for i in range(n):
        currentStart = intervals[i][0]
        currentEnd = intervals[i][1]

        if len(mergedIntervals) == 0 or currentStart > mergedIntervals[-1][1]:
            mergedIntervals.append(intervals[i])
        else:
            mergedIntervals[-1][1] = max(mergedIntervals[-1][1], currentEnd)

    return mergedIntervals

  #firstly I sorted intervals based on the start values and then iterated through them
  #I merged intervals if they overlap else i added as seperate intervals
