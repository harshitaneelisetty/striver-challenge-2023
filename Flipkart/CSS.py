# https://leetcode.com/problems/custom-sort-string/description/

class Solution(object):
    def customSortString(self, order, s):
        s1 = ""
        for i in order:
            if i in s:
                s1 += i * (s.count(i))
        for i in s:
            if i not in s1:
                s1 += i * (s.count(i))
        return s1
