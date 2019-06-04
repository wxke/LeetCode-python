通过删除字母匹配到字典里最长单词
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d = sorted(d,reverse=True)
        d = sorted(d,key = lambda x: len(x))
        lens = len(s)
        for i in d[::-1]:
            j = 0
            q = 0
            leni = len(i)
            while q < lens:

                if i[j] == s[q]:
                    j+=1
                q += 1
                if j == leni:
                    return i
        
        return ''
