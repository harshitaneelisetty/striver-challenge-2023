# https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = [i for i in range(n, 0, -1)]
        frnd = k - 1
        while len(queue) != 1:
            while frnd != 0:
                queue.insert(0, queue.pop())
                frnd -= 1
            queue.pop()
            frnd = k - 1
        return queue[0]
