宝石与石头
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        sum =0 
        for i in J:
            for a in S:
                if i==a:
                    sum = sum +1
        print(sum)
        return sum
