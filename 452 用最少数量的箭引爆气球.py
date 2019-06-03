用最少数量的箭引爆气球
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        len1 = len(points)
        if len1 == 1:
            return 1
        elif len1 == 0:
            return 0
        points = sorted(points,key=lambda x:(x[0],x[1]))
        s = 1
        i = 1
        flag = points[0]
        while i < len1:
            if flag[0]<= points[i][0] <= flag[1]:
                flag=[points[i][0],min(points[i][1],flag[1])]
                i += 1
            else:
                s += 1
                flag = points[i]
                i+=1
                
            
        return s
        
