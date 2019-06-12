任务调度器
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        from collections import Counter
        a = dict(Counter(tasks))
        max1 = max(a.values())
        cout = (list(a.values()).count(max1))
        # print(max1,cout,n,len(tasks))
        return max((n+1) * (max1 - 1) + cout,len(tasks)) 
        
