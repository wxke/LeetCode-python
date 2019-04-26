划分字母区间
class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = [0]
        i = 0
        list1 = []
        long = 0
        x= 0
        while x < len(S):
            j = len(S) - 1
            while i <= j:
                if S[i] not in list1:
                    list1.append(S[i])
                    j = len(S) - 1
                    while j >= i:
                        if S[j] == S[i]:
                            break
                        j = j-1
                    long = max(long,j)
                    j = long
                i = i+1
            res.append(long-x+1)
            x = long+1

        return res[1:]
