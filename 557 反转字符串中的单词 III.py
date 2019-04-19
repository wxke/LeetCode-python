反转字符串中的单词 III
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        list = s.split(" ")

        for i in range(len(list)):
            list[i] = list[i][::-1]
        s=""
        for i in list:
            s = s+i+" "
        s = s.rstrip(" ")
        return s
        
