查找常用字符
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if A == []:
            return []
        len1 = len(A)
        
        if len1 == 1:
            return list(A[0])
        A = sorted(A,key=lambda x:len(x) )
        s = A[0]
        res = []
        for i in s:
            flag = 1
            for j in range(1,len1):
                if i in A[j]:
                    A[j] = A[j].replace(i,"",1)
                    flag += 1
                else:
                    break
            if flag == len1:
                res.append(i)
        
        return res
