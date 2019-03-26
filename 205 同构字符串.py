同构字符串
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        j = 0
        for i in s:
            if i not in dic.keys() and t[j] not in dic.values():
                dic[i]=t[j]
            elif (i in dic.keys() and dic[i] != t[j]) or (i not in dic.keys() and t[j] in dic.values()):
                return False
            j = j+1



        return True
