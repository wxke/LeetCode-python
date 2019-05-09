增减字符串匹配
class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        n = 0
        sum1 = len(S)
        A = []
        for i in range(len(S)):
            if S[i] == 'I':
                A.append(n)
                n = n+1
            elif S[i] == 'D':
                A.append(sum1)
                sum1 -= 1
        
        A.append(sum1)
        return A
