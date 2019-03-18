盛最多水的容器
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        n = r 
        min1 = 0
        while l != r:
            min1 = max(min1,min(height[l],height[r]) * n)
            if height[l] <= height[r]:
                l +=1
            else:
                r -=1
            
            n = n - 1
                
                
        return min1
