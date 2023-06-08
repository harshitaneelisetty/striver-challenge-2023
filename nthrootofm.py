#https://www.codingninjas.com/codestudio/problems/find-nth-root-of-m_8230799?challengeSlug=striver-sde-challenge

import math
def NthRoot(n: int, m: int) -> int:
    root = math.pow(m, 1.0 / n)
    if abs(root - round(root)) < 1e-9:
        return round(root)
    else:
        return -1
      
#I just applied simple math
