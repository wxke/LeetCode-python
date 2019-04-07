最长回文串
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        list1 = set(s)
        list1 = list(list1)
        dic1 = {}
        flag_1 = False
        cont = 0
        for i in list1:
            j = s.count(i)
            dic1[i] = j
            if j % 2 == 0:
                cont += j
            else:
                flag_1 =True
                cont += j -1


        return cont + (1 if flag_1 else 0)
