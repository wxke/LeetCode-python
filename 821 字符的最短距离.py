字符的最短距离
class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        list = []
        for i in range(len(S)):
            left = 0
            right =0
            for j in range(0,i+1)[::-1]:
                if S[j] == C:
                    left = i -j
                    break
                if j ==0:
                    left = 20000
            for j in range(i,len(S)):
                if S[j] ==C:
                    right = j-i
                    break
                if j ==len(S)-1:
                    right = 20000
            if left <=right:
                list.append(left)
            else:
                list.append(right)
                
        return list
