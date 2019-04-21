在系统中查找重复文件
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = {}
        for i in paths:
            q= i.split(" ")
            for j in range(1,len(q)):
                k = q[j].index('(')
                text = q[j][k+1:-1]
                if text in dic:
                    k = q[0]+"/"+q[j][:k]
                    dic[text].append(k)
                else:
                    k = q[0]+"/"+q[j][:k]
                    dic[text] = [k]
        
        res = []
        for k,v in dic.items():
            if len(v) != 1:
                res.append(v)
        
        return res
            
