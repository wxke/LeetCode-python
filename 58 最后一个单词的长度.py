最后一个单词的长度
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s =="":
            return 0
        s = s.split(" ")
        res = []
        for i in s:
            if i != "":
                res.append(i)
        if res == []:
            return 0
        return len(res[-1])
