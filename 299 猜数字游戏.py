猜数字游戏
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        len1 = len(secret)
        a = 0
        str1 = []
        str2 = [] 
        for i in range(len1):
            if secret[i] == guess[i]:
                a += 1
            else:
                str1 += secret[i]
                str2 += guess[i]
        
        from collections import Counter
        str1 = dict(Counter(str1))
        str2 = dict(Counter(str2))
        b = 0
        for k in str2:
            if k in str1:
                b += min(str2[k],str1[k])
        
        a = str(a)+"A"+str(b)+"B"    
        return a
        
