两句话中的不常见单词
class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A =A.split()
        B =B.split()
        dict = {}
        for i in A:
            if i in dict:
                dict[i] += 1
            else:
                dict[i]=0
        for i in B:
            if i in dict:
                dict[i] += 1
            else:
                dict[i]=0
        list =[]
        for key,value in dict.items():
            if value ==0:
                list.append(key)
        return list
