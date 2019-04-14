提莫攻击
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        timeSeries = list(set(timeSeries))
        timeSeries.sort()
        if duration == 1:
            return len(timeSeries)
        sum1 = 0
        flag = 0
        for i in range(len(timeSeries)):
            # print(flag)
            if flag < timeSeries[i]:
                # print(1)
                flag = timeSeries[i] + duration -1
                sum1 += duration
                # print(1,sum1)
            elif flag >  timeSeries[i]:
                flag, sum1  = timeSeries[i] + duration -1,sum1 + timeSeries[i] + duration -1 - flag
                # print(2,sum1)
            elif flag == timeSeries[i]:
                # print(3)
                flag = timeSeries[i] + duration -1 
                sum1 += duration -1
                # print(3,sum1)
        return sum1
