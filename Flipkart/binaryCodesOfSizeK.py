# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/description/

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        lst = {s[i : i + k] for i in range(len(s) - k + 1)}
        return len(lst) == 2 ** k
      
    # just counted the subarray of len k if it equal to 2 power k we can simply return true
    # here i taken set becoz not to count duplicates
