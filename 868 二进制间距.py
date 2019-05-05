二进制间距
class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        list = []
        while N:
            list.append(N%2)
            N = N//2
        sum =0
        for i in range(len(list)-1):
            if list[i] == 1:
                for j in range(i+1,len(list)):
                    if list[j] ==1:
                        sum = max(j-i,sum)
                        break
        return sum
