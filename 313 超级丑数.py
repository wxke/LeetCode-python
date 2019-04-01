超级丑数
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        res = [1]
        k = len(primes)
        list1 = [0 for i in range(k)]
        list2 = primes
        for i in range(n - 1):
            num = sys.maxsize
            for j in range(k):
                num = min(num, res[list1[j]] * list2[j])
            res.append(num)
            for j in range(k):
                if res[-1] == res[list1[j]] * list2[j]:
                    list1[j] += 1
        return res[-1]
