构造矩形
class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        w = math.sqrt(area)
        w = int(w)


        for i in range(w,0,-1):
            if area % i == 0:
                return [area//i,i]
