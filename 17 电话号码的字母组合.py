电话号码的字母组合
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        dic = {
            '1':[],
            "2":['a','b','c'],
            "3":['d','e','f'],
            "4":['g','h','i'],
            "5":['j','k','l'],
            "6":['m','n','o'],
            "7":['p','q','r','s'],
            "8":['t','u','v'],
            "9":['w','x','y','z'],
            
        }
        
        
        ans = [i for i in dic[digits[0]]]
        if len(digits) == 1:
            return ans
        for i in range(1,len(digits)):
            res = []
            for x in range(len(ans)):
                for j in range(len(dic[digits[i]])):
                    res.append(ans[x] + dic[digits[i]][j])
            ans = res[::]
        
        return ans 
                
        
