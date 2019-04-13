供暖器
class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.sort()
        houses.sort()
        max1 = 0
        j = 0
        for i in houses:
            while j < len(heaters) -1 and heaters[j] + heaters[j+1] < i*2:
                j +=1
            max1 = max(max1,abs(heaters[j] - i))
        return max1
