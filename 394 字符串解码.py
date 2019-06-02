字符串解码
class Solution:
    def decodeString(self, s: str) -> str:
        str1 = s
        dic = {'0','1','2','3','4','5','6','7','8','9'}
        tmp = 1
        while tmp:
            stack = []
            flag = 0
            tmp = 0
            for i in range(len(s)):
                if s[i] == '[':
                    flag = i
                    stack.append(s[i])
                elif s[i] == ']' and stack[-1] == '[':
                    tmp = 1
                    j = 0
                    for q in range(flag-1,-1,-1):
                        if str1[q] in dic: 
                            j += 1
                        else:
                            break
                    str1 = str1.replace(str1[flag-j:i+1],str1[flag+1:i]*int(str1[flag-j:flag]))                
                    break
            s = str1
        return str1
