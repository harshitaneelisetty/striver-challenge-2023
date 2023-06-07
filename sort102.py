#https://www.codingninjas.com/codestudio/problems/sort-0-1-2_8230695?challengeSlug=striver-sde-challenge

def sort012(arr, n) :
    left = 0
    right = len(arr) - 1
    mid = left
    while mid <= right:
        if arr[mid] == 0:
            arr[left], arr[mid] = arr[mid], arr[left]
            left += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[right] = arr[right], arr[mid]
            right -= 1
    return arr
 
#I used the Dutch National Flag algorithm to sort an array containing only 0s, 1s, and 2s in linear time. 
