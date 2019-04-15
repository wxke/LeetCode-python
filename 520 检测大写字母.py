检测大写字母
class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        sum1 = 0
        for i in word:
            if i == i.upper():
                sum1+=1
                
        if sum1 == len(word) or (sum1==1 and word[0]==word[0].upper() ) or sum1 ==0:
            return True
        else:
            return False
            
        
