每日温度
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        len1 = len(T)
        res = [0 for i in range(len1)]
        
        for i in range(len1-2,-1,-1):
            if T[i] < T[i+1]:
                res[i] = 1
            else:
                j =  i + 1
                flag = False
                while j < len1 - 1:
                    # print(T[i],T[j + res[j]])
                    if res[j] == 0:
                        break
                    elif T[i] >= T[j + res[j]] and res[j] != 0:
                        j = j + res[j]
                    else:
                        flag = True
                        break
                if flag:
                    res[i] = j - i + res[j]
                else:
                    res[i] = 0
        
        return res
                        
                
                        
                    
