#https://www.codingninjas.com/codestudio/problems/job-sequencing-problem_8230832?challengeSlug=striver-sde-challenge


def jobScheduling(jobs):
    jobs.sort(key=lambda x: (-x[1], -x[0]))
    maxProfit = 0
    maxDeadline = 0

    for i in range(len(jobs)):
        maxDeadline = max(maxDeadline, jobs[i][0])

    slots = []

    for i in range(1, maxDeadline + 1):
        slots.append(i)

    maxProfit = 0
    for i in range(len(jobs)):
        if len(slots) == 0 or jobs[i][0] < slots[0]:
            continue

        availableSlot = slots[bisect.bisect(slots, jobs[i][0]) - 1]
        maxProfit += jobs[i][1]
        slots.remove(availableSlot)

    return maxProfit

  #I sorted jobs based on their decreasing deadlines and profits
  # then I itersted through the sorted list and selects jobs based on the availability of slots
  # added their profits to the total maximum profit. 
  
 




