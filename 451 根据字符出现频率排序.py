根据字符出现频率排序
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = collections.Counter(s)
        li = []
        for i in dic.items():
            li.append((i[0],i[1]))
        li.sort(key=lambda i:i[1])
        ans = ""
        for i in li:
            ans += i[0] * i[1]
        return ans[::-1]
