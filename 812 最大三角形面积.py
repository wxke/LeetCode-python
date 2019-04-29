最大三角形面积
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        max1 = 0
        sum1 = 0
        for i in range(len(points) - 2):
            for j in range(i + 1, len(points) - 1):
                for p in range(i + 2, len(points)):
                    # S=(1/2)*(x1y2+x2y3+x3y1-x1y3-x2y1-x3y2)
                    sum1 = (1 / 2.0) * abs(points[i][0] * points[j][1] + points[j][0] * points[p][1] + 
                        points[p][0] * points[i][1] -points[i][0] * points[p][1] - points[j][0] * points[i][1] - 
                        points[p][0] * points[j][1])

                    max1 = max(sum1, max1)
                    
        return max1
