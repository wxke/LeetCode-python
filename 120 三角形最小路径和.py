三角形最小路径和
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        list1 = [[0 for i in range(len(triangle))] for j in range(len(triangle))]
        list1[0][0] = triangle[0][0]
        for i in range(1,len(triangle)):
            len1 = len(triangle[i])
            for k,v in enumerate(triangle[i]):
                left = k - 1
                right = k
                if k == 0:
                    list1[i][k] = list1[i-1][k] + triangle[i][k]
                elif k == len1 - 1:
                    list1[i][k] = list1[i-1][k-1] +triangle[i][k]
                else:
                    list1[i][k] = triangle[i][k] + min(list1[i-1][k-1],list1[i-1][k])
                
        return min(list1[-1])
              
                
