查找和替换模式
class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        a = []
        len1 = len(set(pattern))
        for i in words:
            dic = {}
            flag = True
            for j in range(len(i)):
                if i[j] not in dic.keys():
                    dic[i[j]] = pattern[j]
                else:
                    if dic[i[j]] != pattern[j]:
                        flag = False
                        break
            if flag:
                if len(set(dic.keys())) == len(set(dic.values())):
                    a.append(i)
        
        return a
