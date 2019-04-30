较大分组的位置
class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        flag = S[0]
        sum1 = 0
        list1 = []
        S = S + '1'
        index = 0
        for i in range(len(S)):
            if S[i] == flag:
                sum1 += 1
            else:
                if sum1 >=3:
                    list1.append([index,i-1])
                flag = S[i]
                sum1 = 1
                index = i
        return list1
