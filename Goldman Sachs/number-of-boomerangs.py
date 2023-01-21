#https://leetcode.com/problems/number-of-boomerangs/description/

class Solution:
    def distance(self, p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return 0
        ans = 0
        for i in range(len(points)):
            hashMap = defaultdict(int)
            for j in range(len(points)):
                if i != j:
                    dis = self.distance(points[i], points[j])
                    hashMap[dis] += 1
                       
            for k in hashMap:
                if hashMap[k] > 1:
                    ans += hashMap[k] * (hashMap[k] - 1)
        return ans
      
      #for each point I created a hashmap
      #and counted all points with same distance. 
      #If for a point i, there are k points with distance dis
      #I traversed hashMap to find number of boomerangs
      #number of boomerangs corresponding to that are k * (k - 1) and added that to the ans
     
