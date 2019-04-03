加油站
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        
        res = 0
        start = 0
        sum1 = 0
    
        for i in range(len(gas)):
            sum1 += (gas[i] - cost[i])
            res += (gas[i] - cost[i])
            if sum1 < 0 :
                start = i + 1
                sum1  = 0
                
        # print(res)
        return start if res >= 0 else -1
                    
        
