单词模式
class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split()
        if len(str) != len(pattern):
            return False
        dic = dict(zip(pattern,str))
        return len(dic.keys()) == len(set(str)) and len(set(dic.values())) == len(set(str))
