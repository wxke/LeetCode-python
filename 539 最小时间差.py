最小时间差
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
         
        a = sorted(timePoints)
        min1 = 720
        for i in range(0,len(a)):
            a[i] = a[i].split(":")
            a[i][0] = int(a[i][0])
            a[i][1] = int(a[i][1])
        
        for i in range(1,len(a)):

            min1 = min(min1,(a[i][0] - a[i-1][0]) * 60 + a[i][1] - a[i-1][1])

        min1 = min(min1,(a[0][0] + 24 - a[-1][0]) * 60 + a[0][1] - a[-1][1])

        return min1
                
            
            
