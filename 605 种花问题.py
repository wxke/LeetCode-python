种花问题
class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed.append(0)
        flowerbed.insert(0,0)
        if n == 0:
            return True
        for i in range(1,len(flowerbed)-1):
            if (flowerbed[i-1] | flowerbed[i] | flowerbed[i+1]) == 0:
                n = n -1
                flowerbed[i] = 1
            if n == 0:
                return True

        return False
