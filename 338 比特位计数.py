比特位计数
class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        list1 = [0 for i in range(num+1)]
        for i in range(1,num+1):
            n = i
            cont = 0
            if list1[i] == 0:
                while n:
                    n = n & (n-1)
                    cont += 1
                while i <num+1:
                    list1[i] = cont
                    i = i << 2
        return  list1
