最大单词长度乘积
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        list1 = []
        len1 = len(words)
        q = words[::]
        for i in range(len1):
            words[i] = set(words[i])
        max1 = 0
        for i in range(len1):
            for j in range(i+1,len1):
                if words[i] & words[j] == set():
                    max1 = max(max1,len(q[i]) * len(q[j]))
        return max1
                    
                    
            
