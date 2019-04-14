神奇字符串
class Solution:
    def magicalString(self, n: int) -> int:
        s = [1,2,2]
        flag = 1
        s2 = [1,2]
        cot = 2
        ind = 2
        while cot < n:
            s2.append(s[ind])
            for i in range(s2[ind]):
                s.append(flag)
            cot += s2[ind]
            if flag == 1:
                flag = 2
            else:
                flag =1 
            ind += 1
        return s[:n].count(1)
            
        
        
