森林中的兔子
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        if answers == []:
            return 0
        dic = {}
        for k in answers:
            if k not in dic:
                dic[k] = 1
            else:
                dic[k] += 1
        
        
        sum1 = 0
        for k,v in dic.items():
            while v >0:
                print(k,v)
                if k == 0:
                    sum1 += v
                    v = 0
                elif k < v:
                    sum1 += k + 1
                    v = v - k -1
                elif k >= v:
                    sum1 += k + 1
                    v = 0
        
        return sum1
                
                
            
        
        
