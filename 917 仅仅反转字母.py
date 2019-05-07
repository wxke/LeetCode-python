仅仅反转字母
class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        S = list(S)
        q = S[::-1]
        j = 0
        i = 0
        while i < len(S) and j <len(S):
            if 'a' <= q[j] <= 'z' or 'A' <= q[j] <= 'Z':
                if 'a' <= S[i] <= 'z' or 'A' <= S[i] <= 'Z':
                    S[i] = q[j]
                    i += 1
                    j +=1
                else:
                    i +=1
            else:
                j +=1
        return ''.join(S)
