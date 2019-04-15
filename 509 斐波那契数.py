斐波那契数
class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1
        list1 = [0,1]
        for i in range(2,N+1):
            list1.append(list1[i-1] + list1[i-2])
        return list1[-1]
