#https://www.codingninjas.com/codestudio/problems/maximum-meetings_8230795?challengeSlug=striver-sde-challenge

def compare(a, b):
    if a[2] == b[2]:
        if a[0] < b[0]:
            return -1
        return 1
    else:
        if a[2] < b[2]:
            return -1
        return 1


def maximumMeetings(start, end):
    n = len(start)
    meetings = [defaultdict(int) for i in range(n)]

    for i in range(n):
        meetings[i][0] = i + 1
        meetings[i][1] = start[i]
        meetings[i][2] = end[i]

    meetings = sorted(meetings, key=functools.cmp_to_key(compare))
    result = []
    result.append(meetings[0][0])
    current_time = meetings[0][2]

    for i in range(n):
        if meetings[i][1] > current_time:
            result.append(meetings[i][0])
            current_time = meetings[i][2]

    return result
  
  #i sorted the meetings based on their end times
  #ans i selected the maximum number of non-overlapping meetings
  #by iteratively choosing meetings whose start times are after the end time of the previously selected meeting.
  #i created a result list which contains list of indices representing the maximum set of non-overlapping meetings.
  

  
