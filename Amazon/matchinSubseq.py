# https://leetcode.com/problems/number-of-matching-subsequences/

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        wordDict = defaultdict(list)
        for i in words:
            wordDict[i[0]].append(i)
        count = 0
        for char in s:
            x = wordDict[char]
            wordDict[char] = []
            for i in x:
                if len(i) == 1:
                    count += 1
                else:
                    wordDict[i[1]].append(i[1 : ])
        return count
