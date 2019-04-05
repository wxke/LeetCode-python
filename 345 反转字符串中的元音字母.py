反转字符串中的元音字母
class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        j = len(s)-1
        s1 = list(s)
        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU' and i < j:
                for q in range(j,0,-1):
                    if s[q] in 'aeiouAEIOU':
                        j =q
                        s1[i] ,s1[j] = s1[j] ,s1[i]
                        j = j-1
                        break
            elif i >=j :
                break
        return ''.join(s1)
